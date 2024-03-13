from slowapi import Limiter
from fastapi import HTTPException
from api.utils.api_key_auth import get_api_key

limiter = Limiter(key_func=get_api_key)

def rate_limit_exceeded_handler(request, exc):
    return HTTPException(status_code=429, detail="Rate limit exceeded")