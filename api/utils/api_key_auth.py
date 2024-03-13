from fastapi import HTTPException
from typing import Optional

async def get_api_key(api_key: Optional[str] = None):
    if api_key is None:
        raise HTTPException(status_code=400, detail="API key is required")
    # ToDo: Validate api key
    return api_key