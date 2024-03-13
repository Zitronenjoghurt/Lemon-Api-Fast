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
Will return a random image of the specified category.

This will stream the image, it is intended to just get a grasp of the images in the browser.

The image will be unable to be embedded, use /images/random/category/redirect instead
""",
    "get_random_image_url_by_category":
"""
Will return a random image URL of the specified category.
""",
    "redirect_to_random_image":
"""
Will redirect to a random image of the specified category on my static image API.

That way youre able to embed the random image, though it will be less viable to refresh over and over again in browser to see different images.

Example: https://image.lemon.industries/hug-1.gif
"""
}