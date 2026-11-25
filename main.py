"""Decode the bundled base64 entry image and write it to the output directory.

The competition entry image is stored in this repository as base64 text in
``entry.png.b64`` (next to this program) rather than as a binary file. This
program decodes that text and writes the resulting PNG to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when the variable is unset).
"""

import base64
import os

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(here, "entry.png.b64")
    with open(b64_path, "r", encoding="ascii") as f:
        text = f.read()
    data = base64.b64decode(text, validate=True)
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("decoded data does not start with the PNG signature")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
