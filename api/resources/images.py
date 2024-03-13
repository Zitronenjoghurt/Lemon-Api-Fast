from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from api.constants.image_library import IMAGE_LIBRARY, CATEGORIES
from api.data.doc_metadata import resource_descriptions
from api.models.image_names_response import ImageNamesResponse
from api.models.url_response import UrlResponse
from api.utils.file_operations import get_image_path
from api.utils.html_operations import get_image_type
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
        "count": IMAGE_LIBRARY.category_counts[category],
        "image_names": IMAGE_LIBRARY.files_by_category[category]
    }
    return ImageNamesResponse(**data)
# endregion

# region get_random_image_by_category
@router.get(
    "/images/random/{category}", 
    tags=["images"],
    summary="Returns a random category image | LIMIT: 1/sec",
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

# region get_random_image_url_by_category
@router.get(
    "/images/random/{category}/url", 
    tags=["images"],
    summary="Get a random image url of a category | LIMIT: 1/sec",
    description=resource_descriptions["get_random_image_url_by_category"],
    responses={
        404: {"description": "Category Not Found"},
        429: {"description": "Rate limit exceeded"}
    }
)
@limiter.limit("1/second")
async def get_random_image_url_by_category(category: str, request: Request) -> UrlResponse:
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found.")
    file_name = IMAGE_LIBRARY.get_random_by_category(category=category)
    return UrlResponse(url=f"https://image.lemon.industries/{file_name}")
# endregion

# region redirect_to_random_image
@router.get(
    "/images/random/{category}/redirect", 
    tags=["images"],
    summary="Redirect to a random image of a category | LIMIT: 1/sec",
    description=resource_descriptions["redirect_to_random_image"],
    responses={
        307: {"description": "Redirect to the image on static image API"},
        404: {"description": "Category Not Found"},
        429: {"description": "Rate limit exceeded"}
    }
)
@limiter.limit("1/second")
async def redirect_to_random_image(category: str, request: Request) -> RedirectResponse:
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found.")
    file_name = IMAGE_LIBRARY.get_random_by_category(category=category)
    url = f"https://image.lemon.industries/{file_name}"
    return RedirectResponse(url=url)
# endregion

# region embed_random_image
@router.get(
    "/images/random/{category}/embed", 
    tags=["images"],
    summary="Retrieve random image of category for embedding | LIMIT: 1/sec",
    description=resource_descriptions["embed_random_image"],
    responses={
        404: {"description": "Category Not Found"},
        429: {"description": "Rate limit exceeded"}
    }
)
@limiter.limit("1/second")
async def embed_random_image(category: str, request: Request) -> HTMLResponse:
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found.")
    
    file_name = IMAGE_LIBRARY.get_random_by_category(category=category)
    image_url = f"https://image.lemon.industries/{file_name}"
    image_type = get_image_type(file_name=file_name)
    title = category.capitalize()

    # ToDo: determine dimensions of the image and append it to the header
    html_content = f"""
    <html>
        <head>
            <title>Random {title} Image</title>
            <meta property="og:title" content="Random {title} Image" />
            <meta property="og:image" content="{image_url}" />
            <meta property="og:image:type" content="{image_type}" />
            <meta property="og:url" content="{image_url}" />
            <meta property="og:type" content="image" />
            <meta property="og:site_name" content="Lemon Industries" />
            <meta name="theme-color" content="#CEF562" data-react-helmet="true" />
        </head>
        <body>
            <img src="{image_url}" alt="Random {title} Image" />
        </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)
# endregion