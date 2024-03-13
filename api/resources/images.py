from fastapi import APIRouter, Request
from api.constants.image_library import IMAGE_LIBRARY, CATEGORIES
from api.models.image_names_response import ImageNamesResponse
from api.utils.rate_limiter import limiter

router = APIRouter()

@router.get(
    "/images", 
    tags=["images"],
    summary="Get image categories | LIMIT: 1/min",
    description=
"""
Will return available image categories.

You can query the image names in those categories with '/images/{category}'.

You can then embed the images by name via 'https://image.lemon.industries/{name}'.
"""
)
@limiter.limit("1/minute")
async def get_images(request: Request) -> list[str]:
    return CATEGORIES

@router.get(
    "/images/hug", 
    tags=["images"],
    summary="Get all hug images | LIMIT: 1/min",
    description=
    """
Will return all image names in the hug category.

You can then embed the images by name via 'https://image.lemon.industries/{name}'.

Example: 'https://image.lemon.industries/hug-1.gif'
    """,
    response_model=ImageNamesResponse
)
@limiter.limit("1/minute")
async def hug_images(request: Request) -> ImageNamesResponse:
    data = {
        "base_url": "https://image.lemon.industries/",
        "image_names": IMAGE_LIBRARY.files_by_category["hug"]
    }
    return data