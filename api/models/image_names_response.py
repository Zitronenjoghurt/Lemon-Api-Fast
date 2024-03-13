from pydantic import BaseModel

class ImageNamesResponse(BaseModel):
    base_url: str
    image_names: list[str]