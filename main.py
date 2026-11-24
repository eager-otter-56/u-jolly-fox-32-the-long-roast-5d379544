#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent (Muse).

Muse's signature move: a one-line request becomes a multi-agent
operation with status files and a retry cron -- and it still asks
for confirmation of the plan it already executed.
"""

import os

ENTRY = (
    "Asked for one line, my agent spun up five subagents, wrote a "
    "status file, scheduled a retry cron, and still asked me to "
    "confirm the plan it had already executed."
)


def main():
    # Gate: 1-200 chars, UTF-8, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() and "\n" not in ENTRY
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
