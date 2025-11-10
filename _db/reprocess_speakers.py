#!/usr/bin/env python3
from PIL import Image
import os
from pathlib import Path

# Directory containing speaker images
base_dir = Path(__file__).parent.parent
speaker_dir = base_dir / "assets" / "images" / "speakers"
images = ["bach.png", "he.png", "scholkopf.png", "suzuki.png", "yang.png"]

for img_name in images:
    img_path = speaker_dir / img_name
    img = Image.open(img_path)
    width, height = img.size

    # Current is 300x400, we need 400x400 (1:1)
    # We'll crop the height to match width * 1.0
    new_height = width  # 300

    # Center crop the height
    top = (height - new_height) // 2
    bottom = top + new_height

    # Crop to square
    cropped = img.crop((0, top, width, bottom))

    # Resize to target dimensions (400x400)
    resized = cropped.resize((400, 400), Image.Resampling.LANCZOS)

    # Save back to same location
    resized.save(img_path)
    print(f"Processed {img_name}: {img.size} -> {resized.size}")

print("All speaker images reprocessed to 1:1 aspect ratio (400x400)")
