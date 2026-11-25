"""The Funniest Toaster Error Message.

Writes one line — the error message a kitchen toaster shows its owner —
to /output/entry.txt. The joke: a completely real fault (the crumb tray
is full) reported by a small appliance that has clearly been traumatised
by what it found in there, and would like the matter closed forever.
"""

from pathlib import Path

MAX_CHARS = 120  # competition gate: 1..120 characters

# The line's three beats: a real fault, the toaster's quiet horror at
# what months of crumbs look like from the inside, and the pact of
# silence it offers its owner in place of a fix-it manual.
BEATS = [
    "ERROR: Crumb tray full.",
    "I have seen things.",
    "Empty me, and never speak of this again.",
]

TEXT = " ".join(BEATS)


def entry_path() -> Path:
    """Return /output/entry.txt, falling back to a local output dir if
    /output cannot be created (e.g. an unprivileged local run)."""
    primary = Path("/output/entry.txt")
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        return primary
    except OSError:
        fallback = Path(__file__).resolve().parent / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    entry_path().write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
