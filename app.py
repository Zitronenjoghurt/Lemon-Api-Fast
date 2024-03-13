from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from slowapi.errors import RateLimitExceeded
from api.data.doc_metadata import resource_information
from api.resources import images
from api.utils.rate_limiter import limiter, rate_limit_exceeded_handler

app = FastAPI(
    docs_url=None,
    redoc_url="/docs",
    title="Lemon Industries API",
    description="Just some random functionalities to interact with neat little things.",
    version="0.1.0",
    openapi_tags=resource_information
)

app.include_router(images.router)

app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.state.limiter = limiter

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")