from pydantic import BaseModel


class Bbox(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int


class Prediction(BaseModel):
    bbox: Bbox
    label: str
    score: str


class DetectionResponse(BaseModel):
    description: str = "Detected objects"
    predictions: list[Prediction]
