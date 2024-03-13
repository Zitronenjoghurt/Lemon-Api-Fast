from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from api.resources import images
from api.utils.rate_limiter import limiter, rate_limit_exceeded_handler

app = FastAPI()

app.include_router(images.router)

app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.state.limiter = limiter