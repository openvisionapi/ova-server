from abc import ABC, abstractmethod


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
    def detection(self, model_name, image):
        pass
