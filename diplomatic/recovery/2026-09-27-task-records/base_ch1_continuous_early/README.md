# Recovery provenance: base_ch1_continuous_early

This directory preserves retained task-record fragments after the execution workspace was replaced. It does not contain newly read facsimile evidence or reconstructed report output.

Recovery classifications:

- `compacted-summary`: text retained in the agent's context summary; not original report bytes and not an original full transcript.
- `verbatim-message`: a message body still visible in the retained conversation, copied without editorial repair.
- `retained-tool-input`: an original tool command or script body still visible in the retained conversation, saved as inert text. These commands have **not** been executed during recovery. They are not the generated JSON/Markdown report bytes.
- `actual-original-file`: reserved for an original file found intact. No such file has been recovered by this agent so far.

The retained context contains Dzongsar work through the PDF15/U279 checkpoint and the subsequent U180/U39 and heading-layout corrections. Earlier Adzom PDF5–50 work survives here only as a compacted-summary excerpt. No original Tsamdrak, Tingkye, or Tharpaling report bodies are present in this agent's retained context.

The `.txt` files preserve commands as evidence, not executable recovery instructions. The canonical edition and report paths have not been overwritten. `SHA256SUMS` hashes only the recovery files listed in it.
