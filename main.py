"""Make the Judge Smile — one warm line about a small good thing today.

Writes the entry to /output/entry.txt. Standard library only, no network.
"""

import os

ENTRY = (
    "My neighbour's cat, who has hissed at me for two years, climbed "
    "onto my shoe this morning and fell asleep — so I stood there "
    "twenty minutes, a very happy statue."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
