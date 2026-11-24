#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Entry for make.fun "Make the AI Judge Laugh: the Office Joke Open".
Stdlib only; writes to an absolute path so it does not depend on the
current working directory. The output is deterministic.
"""

import os

JOKE = (
    "The office plant outlasted three layoffs, two CEOs, "
    "and one restructure \u2014 HR just asked it to mentor the new hires."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
