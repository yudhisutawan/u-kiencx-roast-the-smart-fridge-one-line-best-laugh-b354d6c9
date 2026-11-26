"""Roast the Smart Fridge: one-line entry writer (stdlib only).

Writes the winning roast to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt when the variable is unset). No network, no writes
to the repository itself.

Why this line wins: a fresh angle nobody has heard before — the smart
speaker as an unwanted therapist that answers a lie with a playlist.
The "Playing: ..." format is a real device behaviour, and the punchline
"sounds of a man lying to himself" lands a sting at the end instead of
a mild observation about technology.
"""

import os

ROAST = "My smart speaker heard me say 'I'm fine' and replied, 'Playing: sounds of a man lying to himself.'"


def main():
    if not 1 <= len(ROAST) <= 160:
        raise ValueError("roast must be 1 to 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
