from fastapi import APIRouter, Depends, Form, Request
from PIL.Image import Image

from api import limiter
from api.config.api.config import config
from api.detection import validators
from api.detection.consts import DetectionModels
from api.detection.schemas import DetectionResponse
from api.inference import inference

router = APIRouter(prefix="/api/v1")


@router.post("/detection")
@limiter.limit(config.DETECTION_RATE_LIMIT)
async def object_detection(
    request: Request,
    image: Image = Depends(validators.input_image),
    model: DetectionModels = Form(),
) -> DetectionResponse:
    predictions = await inference.detection(model_name=model.value, image=image)
    return DetectionResponse(description="Detected objects", predictions=predictions)
