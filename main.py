"""One-line cat joke entry for make.fun.

Writes a single joke line to /output/entry.txt with no trailing newline.
"""

import os

JOKE = "My cat knocked my coffee off the table, looked me dead in the eye, and purred - honestly, he's management material."


def main():
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"joke must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "joke must be a single line"
    assert line.strip(), "joke must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify the file holds exactly the line, with no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt content mismatch"
    print(f"OK: {len(line)} chars written to /output/entry.txt")


if __name__ == "__main__":
    main()
