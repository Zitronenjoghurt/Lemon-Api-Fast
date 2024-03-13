import os
from pathlib import Path
from typing import Optional

ROOT_DIR = str(Path(__file__).parent.parent.parent)
ROOT_PARENT_DIR = str(Path(__file__).parent.parent.parent.parent)

IMAGE_API_DIR = os.path.join(ROOT_PARENT_DIR, "image_api")

def files_in_directory(path: str, suffix: Optional[str] = None) -> list[str]:
    if not os.path.exists(path):
        raise ValueError(f"Directory {path} does not exist.")
    
    files = []
    for file in os.listdir(path):
        if suffix is not None:
            if suffix in file:
                files.append(file)
        else:
            files.append(file)
    return files

def get_all_api_images() -> list[str]:
    return files_in_directory(path=IMAGE_API_DIR)

def get_image_path(file_name: str):
    return os.path.join(IMAGE_API_DIR, file_name)