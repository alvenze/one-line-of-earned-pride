"""One Line of Earned Pride: writes the entry line to /output/entry.txt."""

from pathlib import Path

ENTRY = (
    "His wife always did the braids; this morning his thick fingers got "
    "their daughter's plait to hold to the very end, and she checked the "
    "mirror and didn't fix it."
)

OUTPUT = Path("/output/entry.txt")

# The bounty gate: UTF-8 text of 1 to 240 characters, not only white
# space, on a single line. The program refuses to write a line that
# would fail it, so an edit to ENTRY can never silently disqualify the
# entry.
MIN_CHARS = 1
MAX_CHARS = 240


def check_gate(text: str) -> None:
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, outside the gate")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_gate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT.read_text(encoding="utf-8")
    if written != ENTRY:
        raise ValueError("written file differs from the entry line")


if __name__ == "__main__":
    main()
