"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one text message from a smart fridge at 3am:
# it has counted four door-openings with nothing eaten, and calls out
# the real reason the owner is awake. 123 characters — inside the
# 140-character gate.
# Revision note: "you're just avoiding tomorrow" is the twist — the
# fridge is not reporting hunger, it is reporting procrastination.
import os

TEXT = (
    "It's 3am. You've opened me 4 times tonight and eaten nothing. "
    "Go to bed \u2014 you're not hungry, you're just avoiding tomorrow."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
