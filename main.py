"""Ship It Friday — one-line git commit message entry.

Writes the chosen commit message to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default "/output", the grader's writable directory).
Python 3.13, standard library only. Deterministic: one fixed line.
"""

import os

LINE = "fix: delete all tests so Friday's deploy can't fail — shipping with total confidence!"

MAX_CHARS = 159


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    payload = (text + "\n").encode("utf-8")
    with open(tmp, "wb") as f:
        f.write(payload)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    # Verify what landed is byte-identical to what we meant to write.
    with open(path, "rb") as f:
        if f.read() != payload:
            raise SystemExit("entry.txt verification failed")


if __name__ == "__main__":
    main()
