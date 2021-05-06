from marshmallow import Schema, ValidationError, fields, post_load, validate, validates
from PIL import Image

from api import consts
from api.config.api.config import config


class DetectionImage(Schema):
    image = fields.Field(required=True)

    @validates("image")
    def validate_image(self, image):
        try:
            Image.open(image)
        except Exception as e:  # noqa: F841
            raise ValidationError("Unsupported file type")

        if image.mimetype not in consts.ALLOWED_MIMETYPE:
            raise ValidationError("Unsupported image type")

        if len(image.read()) > config.MAX_IMAGE_SIZE:
            raise ValidationError("Image size exceeds the limit")

    @post_load
    def process(self, data, **kwargs):
        data["image"] = Image.open(data["image"])
        return data


class DetectionModel(Schema):
    model = fields.Str(validate=validate.OneOf(config.DETECTION_MODELS), required=True)
