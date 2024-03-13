from fastapi import APIRouter, Depends, Request
from api.utils.api_key_auth import get_api_key
from api.utils.rate_limiter import limiter

router = APIRouter()

@router.get("/images")
@limiter.limit("5/minute")
async def get_images(request: Request, api_key: str = Depends(get_api_key)):
    return {"message": "Hello, World!"}