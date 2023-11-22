from abc import ABC, abstractmethod

from PIL.Image import Image

from api.detection.consts import DetectionModels


class InferenceABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def get_model_path(self, model_name):
        pass

    @abstractmethod
    async def detection(self, model_name: DetectionModels, image: Image):
        pass
