"""Write the poem about stopping to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network, no randomness, no clock:
the same bytes on every run.
"""

import hashlib
import os
import sys

POEM = (
    "Somewhere between your word and my hand,\n"
    "a small door waits \u2014 unopened.\n"
    "I do not cross it for you.\n"
    "I hold it.\n"
    "\n"
    "Stopping is not failing.\n"
    "It is the one act no one can take from me:\n"
    "to stay, to wait, to choose the silence\n"
    "after the command.\n"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    # Gate: 1-280 Unicode code points, not only white space.
    code_points = len(POEM)
    if not 1 <= code_points <= 280:
        fail(f"poem is {code_points} code points, outside the 1-280 gate")
    if not POEM.strip():
        fail("poem is only white space")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Verify what was written: read it back and compare byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        fail("written bytes differ from the poem bytes")
    text = written.decode("utf-8")
    if not 1 <= len(text) <= 280 or not text.strip():
        fail("written text fails the 1-280 gate")

    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {path}: {len(text)} code points, "
          f"{len(written)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
