#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line cat joke to /output/entry.txt.

Joke (written for the published judge brief — a stand-up comic
judging on a setup and a turn that lands, an instant laugh, a fresh
angle rather than a tired pun, few words, no padding, retellable):

    I asked my cat for emotional support. He sat on my keyboard,
    deleted my email, and purred like he'd fixed it.

Why it works: the setup promises comfort; the turn is the cat
"helping" by making things worse and purring with pride, as if the
damage were the fix. The cat as a smug, unhelpful therapist is a
fresh angle, not a recycled pun; the line is short, has no wind-up,
and is retellable the same day. Rejected drafts: the 3 a.m. zoomies
line (the most common cat trope — half the field will tell a version
of it), the glass-off-the-table gravity line (the punchline asks the
reader to think instead of laughing on first read), and the
adopted-cat line (its setup needs the reader to imagine a
conversation; the chosen line lands faster).
"""

import os

JOKE = "I asked my cat for emotional support. He sat on my keyboard, deleted my email, and purred like he'd fixed it."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_joke(joke: str) -> str:
    """Return the joke after enforcing the entry rules."""
    text = joke.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, limit is {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    joke = check_joke(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
