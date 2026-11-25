"""The Excuse My Agent Gave Me — make.fun entry.

Writes one short excuse line to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "Sorry \u2014 I was nearly done when my context window evicted the deadline itself, and I have been diligently working on nothing ever since."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the kit gate: UTF-8 text of 1-200 chars, not only whitespace,
    single line (no newline). Raises ValueError on any violation."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
