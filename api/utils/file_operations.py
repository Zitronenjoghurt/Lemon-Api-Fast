import os
from pathlib import Path
from typing import Optional

ROOT_DIR = str(Path(__file__).parent.parent.parent)
ROOT_PARENT_DIR = str(Path(__file__).parent.parent.parent.parent)

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

def get_image_api_directory() -> str:
    return os.path.join(ROOT_PARENT_DIR, "image_api")

def get_all_api_images() -> list[str]:
    path = get_image_api_directory()
    return files_in_directory(path=path)