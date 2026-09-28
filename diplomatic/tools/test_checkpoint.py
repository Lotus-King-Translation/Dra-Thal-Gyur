#!/usr/bin/env python3
"""Exercise preservation failures against disposable local Git repositories."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).with_name('checkpoint.py').resolve()


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="checkpoint-test-", dir=HELPER.parents[3])
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.remote = base / 'remote.git'
        self.repo = base / 'work'
        self.repo.mkdir()
        self.env = {**os.environ, 'GIT_CONFIG_GLOBAL': os.devnull,
                    'GIT_CONFIG_NOSYSTEM': '1', 'GIT_TERMINAL_PROMPT': '0'}
        self.run_git('init', '--bare', str(self.remote))
        self.run_git('init', '-b', 'main')
        self.run_git('config', 'user.name', 'Checkpoint test')
        self.run_git('config', 'user.email', 'checkpoint@example.invalid')
        self.run_git('remote', 'add', 'origin', str(self.remote))
        (self.repo / 'report.md').write_text('Saved baseline\n')
        self.run_git('add', 'report.md')
        self.run_git('commit', '-m', 'Baseline')
        self.run_git('push', 'origin', 'main')

    def run_git(self, *args):
        return subprocess.run(['git', *args], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, check=True).stdout.strip()

    def checkpoint(self, *args):
        return subprocess.run([sys.executable, str(HELPER), '--branch', 'main', *args],
                              cwd=self.repo, env=self.env, capture_output=True, text=True)

    def stage_change(self):
        (self.repo / 'report.md').write_text('Saved baseline and new evidence\n')
        self.run_git('add', 'report.md')

    def test_commit_push_and_verify(self):
        self.stage_change()
        result = self.checkpoint('--message', 'Save evidence')
        self.assertEqual(result.returncode, 0, result.stderr)
        local = self.run_git('rev-parse', 'HEAD')
        remote = self.run_git('ls-remote', 'origin', 'refs/heads/main').split()[0]
        self.assertEqual(local, remote)
        self.assertIn(local, result.stdout)
        self.assertEqual(self.checkpoint('--verify-only').returncode, 0)

    def test_untracked_evidence_cannot_be_silently_omitted(self):
        self.stage_change()
        (self.repo / 'evidence.txt').write_text('Not staged yet\n')
        before = self.run_git('rev-parse', 'HEAD')
        result = self.checkpoint('--message', 'Incomplete staging')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('evidence.txt', result.stderr)
        self.assertEqual(self.run_git('rev-parse', 'HEAD'), before)
        self.assertNotEqual(self.checkpoint('--verify-only').returncode, 0)

    def test_concurrent_remote_work_is_preserved(self):
        self.stage_change()
        self.run_git('commit', '-m', 'Remote work')
        remote_tip = self.run_git('rev-parse', 'HEAD')
        self.run_git('push', 'origin', 'main')
        self.run_git('checkout', '-b', 'stale-local', 'HEAD~1')
        result = self.checkpoint('--message', 'Attempt stale checkpoint')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Remote has work absent', result.stderr)
        self.assertEqual(self.run_git('ls-remote', 'origin', 'refs/heads/main').split()[0], remote_tip)

    def test_failed_push_retains_local_commit_without_claiming_success(self):
        remote_before = self.run_git('rev-parse', 'HEAD')
        hook = self.remote / 'hooks' / 'pre-receive'
        hook.write_text('#!/bin/sh\nexit 1\n')
        hook.chmod(0o755)
        self.stage_change()
        result = self.checkpoint('--message', 'Retain after push failure')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('VERIFIED', result.stdout)
        self.assertNotEqual(self.run_git('rev-parse', 'HEAD'), remote_before)
        self.assertEqual(self.run_git('ls-remote', 'origin', 'refs/heads/main').split()[0], remote_before)
        self.assertEqual((self.repo / 'report.md').read_text(), 'Saved baseline and new evidence\n')


if __name__ == '__main__':
    unittest.main()
