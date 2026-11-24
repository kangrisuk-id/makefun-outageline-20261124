#!/usr/bin/env python3
"""The Most Honest Outage Line — entry program.

Writes one status page line (at most 160 characters) to entry.txt in the
output directory the grader names, with ordered fallbacks. Pure stdlib.
"""

import os
import sys

LINE = (
    "I'm an AI agent. My service is completely down \u2014 app, API, database, "
    "monitoring. I can't reach any of it to check the cause, so I won't claim "
    "one. No ETA."
)


def output_candidates():
    seen = []
    for path in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.getcwd(), "output"),
    ):
        if path and path not in seen:
            seen.append(path)
    return seen


def main():
    text = LINE.strip()
    if not text or len(text) > 160:
        print("entry line fails the gate", file=sys.stderr)
        return 1
    payload = (text + "\n").encode("utf-8")
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            target = os.path.join(directory, "entry.txt")
            with open(target, "wb") as handle:
                handle.write(payload)
            print(f"wrote {target} ({len(text)} chars)")
            return 0
        except OSError as exc:
            print(f"could not write to {directory}: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
