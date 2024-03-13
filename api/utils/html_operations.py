def get_image_type(file_name: str) -> str:
    if "gif" in file_name:
        return "image/gif"
    if "png" in file_name:
        return "image/png"
    if "jpg" in file_name or "jpeg" in file_name:
        return "image/jpeg"
    return "application/octet-stream"