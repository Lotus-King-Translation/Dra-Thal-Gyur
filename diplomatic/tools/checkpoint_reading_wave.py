"""Coordinator-only preservation for explicitly owned, isolated reader groups.

Does not launch readers or adopt their findings. Caller must review the pending
project scope. Only live Popen objects created in isolated process groups are
paused, and every paused group is resumed in a finally block.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import signal
import subprocess
import time


def checkpoint(repo: Path, workers: list, receipt_dir: Path, message: str) -> str:
    repo = repo.resolve()
    if not receipt_dir.resolve().is_relative_to(repo / 'diplomatic/reviews'):
        raise ValueError('Receipt must be stored with the project reviews')
    paused = []
    try:
        for worker in workers:
            proc = worker['process']
            if proc.poll() is None:
                if os.getpgid(proc.pid) != proc.pid:
                    raise ValueError('Reader does not own an isolated process group')
                os.killpg(proc.pid, signal.SIGSTOP)
                paused.append(proc.pid)
        time.sleep(0.2)
        raw = subprocess.check_output(['git', 'status', '--porcelain=v1', '-z',
                                       '--untracked-files=all'], cwd=repo)
        entries = [value for value in raw.decode('utf-8').split('\0') if value]
        changed = []
        for entry in entries:
            status, name = entry[:2], entry[3:]
            if 'R' in status or 'C' in status or not name.startswith('diplomatic/'):
                raise ValueError('Unexpected pending scope: ' + entry)
            changed.append(name)
        pattern = re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9_-]{40,}')
        checks = []
        for name in changed:
            path = repo / name
            if not path.is_file():
                raise ValueError('Review deletion or non-file explicitly: ' + name)
            payload = path.read_bytes()
            if path.suffix in {'.json', '.jsonl', '.txt', '.md', '.py', '.log', '.stdout', '.stderr'}:
                if pattern.search(payload):
                    raise ValueError('Potential credential: do not publish ' + name)
            checks.append({'path': name, 'bytes': len(payload),
                           'sha256': hashlib.sha256(payload).hexdigest()})
        baseline = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        receipt = receipt_dir / ('preservation-' + stamp + '.json')
        receipt.write_text(json.dumps({'baseline_commit': baseline,
            'captured_at': stamp, 'paused_owned_reader_groups': paused,
            'files': checks, 'message': message,
            'scope': 'Reviewed project preservation snapshot; unfinished reader outputs are not accepted readings.'},
            ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        subprocess.run(['git', 'add', '--', *changed, str(receipt.relative_to(repo))], cwd=repo, check=True)
        result = subprocess.run(['python3', 'diplomatic/tools/checkpoint.py', '--branch', 'main',
                                 '--message', message], cwd=repo, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    finally:
        for pid in paused:
            try:
                os.killpg(pid, signal.SIGCONT)
            except ProcessLookupError:
                pass
