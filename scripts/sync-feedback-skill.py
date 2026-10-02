#!/usr/bin/env python3
"""Copy the canonical feedback skill into self-contained plugin packages."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when a packaged skill differs.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "skills/install-feedback/SKILL.md"
    content = source.read_bytes()
    mismatches = []
    for client in ("cursor", "claude"):
        target = root / "plugins" / client / "skills/install-feedback/SKILL.md"
        if args.check:
            if not target.is_file() or target.is_symlink() or target.read_bytes() != content:
                mismatches.append(str(target.relative_to(root)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    if mismatches:
        parser.exit(1, "Run python3 scripts/sync-feedback-skill.py to update:\n" + "\n".join(mismatches) + "\n")
    print("Feedback skill packages match." if args.check else "Feedback skill packages updated.")


if __name__ == "__main__":
    main()
