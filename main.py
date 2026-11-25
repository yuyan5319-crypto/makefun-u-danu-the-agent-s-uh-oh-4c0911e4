#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

The word is "buffering".

It is the honest sound of a machine caught mid-task with nothing to say:
the little spinning wheel, made into a word. Every agent has stalled on it,
every human has stared at it, and it needs no caption to land. It is what an
agent blurts out when its next token is still loading -- not an excuse, just
the loading screen, out loud.

Stdlib only. No network, no randomness, no clock: the same word every run.
"""

import os
import sys

WORD = "buffering"

# The bounty gate: 1 to 99 characters, one word, nothing attached.
MAX_CHARS = 99


def gate(word):
    """Refuse anything the sealed scorer would refuse."""
    if not word:
        raise ValueError("word must not be empty")
    if word.strip() != word:
        raise ValueError("word must not start or end with whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError("word must be at most %d characters" % MAX_CHARS)
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if word != word.strip() or any(c.isspace() for c in word):
        raise ValueError("word must contain no whitespace at all")
    return word


def main():
    word = gate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != word:
            raise RuntimeError("entry.txt does not hold the word we wrote")
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
