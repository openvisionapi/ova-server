import io

from fastapi import File, UploadFile
from PIL import Image

from api import consts, exceptions
from api.config.api.config import config


async def input_image(image: UploadFile = File(...)):
    try:
        im = Image.open(io.BytesIO(image.file.read()))
    except Exception:
        raise exceptions.UnsupportedImageType()

    if image.content_type not in consts.ALLOWED_MIMETYPE:
        raise exceptions.UnsupportedImageType()

    if image.size and image.size > config.MAX_IMAGE_SIZE:
        raise exceptions.ImageTooLarge(
            f"Image size exceeds the limit: {config.MAX_IMAGE_SIZE/(1024*1024)} MB"
        )

    return im
