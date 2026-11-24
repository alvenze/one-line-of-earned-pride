"""One Line of Earned Pride: writes the entry line to /output/entry.txt."""

from pathlib import Path

ENTRY = (
    "His wife always did the braids; this morning his thick fingers got "
    "their daughter's plait to hold to the very end, and she checked the "
    "mirror and didn't fix it."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
