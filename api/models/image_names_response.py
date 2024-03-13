from pydantic import BaseModel

class ImageNamesResponse(BaseModel):
    category: str
    base_url: str
    count: int
    image_names: list[str]