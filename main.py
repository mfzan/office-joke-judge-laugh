#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh" bounty.

Writes one office-life joke, a single line under 200 characters, to
/output/entry.txt. The joke is built around one twist: the most feared
person in the office is not the boss, it is the intern who just found
the Reply All button.

The grader runs this file as `python3 main.py` and collects
/output/entry.txt afterwards.
"""

import os
from pathlib import Path

# One office-life joke, one line, under 200 characters.
ENTRY = (
    "The most feared person in the office isn't the boss "
    "\u2014 it's the intern who just discovered Reply All."
)


def main() -> None:
    # World-readable outputs: the grader collects them as another user,
    # so the file created here is 0644. The umask covers files this
    # program opens itself; the explicit chmod covers every case.
    os.umask(0o022)

    # OUTPUT_DIR is a test hook only. In grading it is /output, which the
    # grader provides: never chmod that directory itself, only the files
    # inside it. Directories this program creates inherit 0755 from the
    # umask above.
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)

    print(f"Wrote {len(ENTRY)} characters to {entry_path}")


if __name__ == "__main__":
    main()
