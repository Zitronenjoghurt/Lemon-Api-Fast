resource_information = [
    {
        "name": "images",
        "description": "Retrieve categories and names of images you can embed wherever you want. They will be mostly anime-themed."
    }
]

resource_descriptions = {
    "get_images": 
"""
Will return available image categories.

You can query the image names in those categories with /images/{category}

You can then embed the images by name via https://image.lemon.industries/{name}
""",
    "get_images_by_category":
"""
Will return all image names in the specified category.

You can then embed the images by name via https://image.lemon.industries/{name}

Example: https://image.lemon.industries/hug-1.gif
""",
    "get_random_image_by_category":
"""
Will redirect to a random image of the specified category.
"""
}