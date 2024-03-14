from PIL import Image
from typing import Optional

def determin_height_width(image_path: str) -> Optional[tuple[int, int]]:
    try:
        with Image.open(image_path) as img:
            return img.size
    except (FileNotFoundError, OSError):
        return