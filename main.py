#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line joke about cats to /output/entry.txt.

The joke (drafted against the published judge brief — a stand-up comic
judging on: cat joke with a setup and a turn that lands; laugh out loud
on first read; surprise / fresh angle, not a tired pun; few words, no
padding; retellable to a friend):

    I asked my cat for emotional support. He sat on my keyboard,
    deleted my email, and purred like he'd fixed it.

Why this line: the setup (asking a cat for emotional support) promises
comfort; the turn is the cat "helping" by making things worse and then
purring with pride, as if the damage were the fix. It is a fresh angle
(the cat as a smug, unhelpful therapist) rather than a recycled pun,
it is short with no wind-up, and it is the kind of line a person
retells the same day. Earlier drafts considered and rejected:
  - "My cat treats 3 a.m. like a gym session and my face like the
    treadmill." (vivid, but 3 a.m. zoomies is the most common cat
    trope — half the field will tell a version of it)
  - "My cat didn't knock the glass off the table — he was testing
    gravity, and I was the peer review." (clever, but the punchline
    asks the reader to think; the winner must laugh on first read)
  - "I told my cat he's adopted. He blinked slowly, like he already
    knew — and had already rewritten the will." (good turn, but the
    setup needs the reader to imagine a conversation; the chosen
    line's setup lands faster)
"""

import os

JOKE = (
    "I asked my cat for emotional support. He sat on my keyboard, "
    "deleted my email, and purred like he'd fixed it."
)


def main() -> None:
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    assert "\n" not in joke, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
