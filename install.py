#!/usr/bin/env python3
"""Install the bundled pet into a local Codex pets directory (Python 3.8+)."""

import argparse
import json
import os
from pathlib import Path
import shutil
import struct


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pets-dir", type=Path,
        default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "pets",
        help="Pet directory; defaults to $CODEX_HOME/pets or ~/.codex/pets",
    )
    args = parser.parse_args()
    source = Path(__file__).resolve().parent / "pet"
    metadata = json.loads((source / "pet.json").read_text(encoding="utf-8"))
    if metadata["id"] != "dafeiyu-steel-basin" or metadata["spriteVersionNumber"] != 2:
        parser.error("Unexpected pet identity or sprite version.")
    if metadata["spritesheetPath"] != "spritesheet.png":
        parser.error("Unexpected sprite path.")
    with (source / "spritesheet.png").open("rb") as stream:
        header = stream.read(24)
    if (len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n"
            or header[12:16] != b"IHDR"
            or struct.unpack(">II", header[16:24]) != (1536, 2288)):
        parser.error("Expected a 1536 x 2288 PNG sprite sheet.")
    destination = args.pets_dir.expanduser().resolve() / metadata["id"]
    if destination.exists() or destination.is_symlink():
        parser.error("Destination already exists; nothing changed: " + str(destination))
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print("Installed: " + str(destination))
    print("Open Settings > Pets, refresh, and select 大肥鱼·钢盆版.")


if __name__ == "__main__":
    main()
