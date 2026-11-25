"""news-image-20261124 v2 entry: write the day's news image to /output/entry.png.

The image lives in this repository as entry.png.b64 (base64 text, because the
GitHub connector cannot push binary files). This program decodes it and writes
the exact PNG bytes to the output directory. It uses only the standard library,
needs no network, and is fully deterministic: every run produces identical bytes.

Local test:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
B64_PATH = HERE / "entry.png.b64"
OUTPUT_NAME = "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    png_bytes = base64.b64decode(B64_PATH.read_text(encoding="ascii"), validate=True)
    if not png_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("entry.png.b64 does not decode to a PNG image")

    output_path = output_dir / OUTPUT_NAME
    output_path.write_bytes(png_bytes)


if __name__ == "__main__":
    main()
