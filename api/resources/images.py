from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import FileResponse
from api.constants.image_library import IMAGE_LIBRARY, CATEGORIES
from api.data.doc_metadata import resource_descriptions
from api.models.image_names_response import ImageNamesResponse
from api.utils.file_operations import get_image_path
from api.utils.rate_limiter import limiter

router = APIRouter()

# region get_images
@router.get(
    "/images", 
    tags=["images"],
    summary="Get image categories | LIMIT: 1/min",
    description=resource_descriptions["get_images"],
    responses={429: {"description": "Rate limit exceeded"}}
)
@limiter.limit("1/minute")
async def get_images(request: Request) -> list[str]:
    return CATEGORIES
# endregion

# region get_images_by_category
@router.get(
    "/images/{category}", 
    tags=["images"],
    summary="Get all images of a category | LIMIT: 5/min",
    description=resource_descriptions["get_images_by_category"],
    response_model=ImageNamesResponse,
    responses={
        404: {"description": "Category Not Found"},
        429: {"description": "Rate limit exceeded"}
    }
)
@limiter.limit("5/minute")
async def get_images_by_category(category: str, request: Request) -> ImageNamesResponse:
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found.")
    data = {
        "category": category,
        "base_url": "https://image.lemon.industries/",
        "image_names": IMAGE_LIBRARY.files_by_category[category]
    }
    return data
# endregion

# region get_random_image_by_category
@router.get(
    "/images/random/{category}", 
    tags=["images"],
    summary="Redirect to a random category image | LIMIT: 1/sec",
    description=resource_descriptions["get_random_image_by_category"],
    responses={
        404: {"description": "Category Not Found"},
        429: {"description": "Rate limit exceeded"}
    }
)
@limiter.limit("1/second")
async def get_random_image_by_category(category: str, request: Request) -> FileResponse:
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found.")
    file_name = IMAGE_LIBRARY.get_random_by_category(category=category)
    path = get_image_path(file_name=file_name)
    return FileResponse(path=path)
# endregion