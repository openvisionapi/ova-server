from flask import Blueprint
from PIL import Image
from webargs.flaskparser import use_kwargs
from werkzeug.wrappers import Response

from api import limiter
from api.config.api.config import config
from api.detection import schemas
from api.inference import inference  # type: ignore
from api.utils import response

detection = Blueprint("detection", __name__, url_prefix="/api/v1")


@detection.route("/detection", methods=["POST"])
@use_kwargs(schemas.DetectionModel(), location="form")
@use_kwargs(schemas.DetectionImage(), location="files")
@limiter.limit(config.DETECTION_RATE_LIMIT)
def object_detection(model: str, image: Image) -> Response:
    predictions = inference.detection(model, image)
    message = {"description": "Detected objects", "predictions": predictions}
    return response(message, 200)
