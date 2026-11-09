#!/usr/bin/env python3
"""Convert the user-supplied original Lampa icon into a Switch NRO JPEG."""
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
source = root / "assets/lampa-original.png"
target = root / "upstream/gx/nx/icon.jpg"
target.parent.mkdir(parents=True, exist_ok=True)

with Image.open(source) as image:
    image.convert("RGB").resize((256, 256), Image.Resampling.LANCZOS).save(
        target, "JPEG", quality=96, subsampling=0
    )

print(f"Original Lampa icon: {source} -> {target}")
