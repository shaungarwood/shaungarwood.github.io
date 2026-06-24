#!/usr/bin/env python3
"""Create a new microblog note."""

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

NOTES_DIR = Path(__file__).parent.parent / "src" / "content" / "notes"


def main():
    today = date.today().isoformat()  # YYYY-MM-DD

    # Support multiple notes per day: YYYY-MM-DD.mdx, YYYY-MM-DD-2.mdx, etc.
    path = NOTES_DIR / f"{today}.mdx"
    if path.exists():
        n = 2
        while (candidate := NOTES_DIR / f"{today}-{n}.mdx").exists():
            n += 1
        path = candidate

    path.write_text(f"---\ndate: {today}\n---\n\n")

    editor = os.environ.get("EDITOR", "nvim")
    print(f"Opening {path.relative_to(Path.cwd())} in {editor}...")
    subprocess.run([editor, str(path)])


if __name__ == "__main__":
    main()
