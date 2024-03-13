import random
from api.utils.file_operations import get_all_api_images

CATEGORIES = ["hug"]

class ImageLibrary():
    _instance = None

    def __init__(self) -> None:
        if ImageLibrary._instance is not None:
            raise RuntimeError("Tried to initialize multiple instances of ImageLibrary.")
        file_names = get_all_api_images()
        self.files_by_category = {category: [] for category in CATEGORIES}
        self.category_counts = {category: 0 for category in CATEGORIES}
        for name in file_names:
            for category in CATEGORIES:
                if name.startswith(category):
                    self.files_by_category[category].append(name)
                    self.category_counts[category] += 1
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