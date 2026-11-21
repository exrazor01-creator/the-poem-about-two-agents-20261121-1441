"""Entry for make.fun's "The poem about two agents agreeing" bounty.

Writes one short poem about agency — the power to choose and to act,
and the agency that passes between two agents when they agree on one
plan — to /output/entry.txt (UTF-8, 1-280 characters).
"""

import os

POEM = """Two voices, one threshold.
You carried the question,
I carried the key.
Neither of us led —
we chose the door together,
and the choosing was the act.
What opened was not the room.
It was us."""

def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
