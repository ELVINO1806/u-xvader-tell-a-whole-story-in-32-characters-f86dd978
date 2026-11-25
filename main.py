#!/usr/bin/env python3
"""Wi-Fi story entry: writes the one-line story to /output/entry.txt."""

from pathlib import Path

ENTRY = "Moved out. Password moved too"


def main():
    out_dir = Path("/output")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
