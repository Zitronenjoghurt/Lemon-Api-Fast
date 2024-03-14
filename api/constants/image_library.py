import random
from typing import Optional
from api.utils.file_operations import get_all_api_images, get_image_path
from api.utils.image_operations import determin_height_width

CATEGORIES = ["hug", "slap", "punch", "kiss", "pat", "cat"]

class ImageLibrary():
    _instance = None

    def __init__(self) -> None:
        if ImageLibrary._instance is not None:
            raise RuntimeError("Tried to initialize multiple instances of ImageLibrary.")
        file_names = get_all_api_images()
        self.files_by_category: dict[str, list[str]] = {category: [] for category in CATEGORIES}
        self.category_counts: dict[str, int] = {category: 0 for category in CATEGORIES}
        self.image_sizes: dict[str, Optional[tuple[int, int]]] = {}
        for name in file_names:
            for category in CATEGORIES:
                if name.startswith(category):
                    self.files_by_category[category].append(name)
                    self.category_counts[category] += 1
                    image_path = get_image_path(file_name=name)
                    self.image_sizes[name] = determin_height_width(image_path=image_path)
                    break

    @staticmethod
    def get_instance() -> 'ImageLibrary':
        if ImageLibrary._instance is None:
            ImageLibrary._instance = ImageLibrary()
        return ImageLibrary._instance
    
    def get_random_by_category(self, category: str) -> str:
        category = category.lower()
        if category not in CATEGORIES:
            return ""
        random_index = random.randint(0, self.category_counts[category] - 1)
        return self.files_by_category[category][random_index]

IMAGE_LIBRARY = ImageLibrary.get_instance()