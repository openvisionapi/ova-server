from importlib import import_module
from pathlib import Path

import tensorflow as tf
from PIL.Image import Image

from api.config.api.config import config
from api.detection import consts
from api.inference.base import InferenceABC


class TensorflowInference(InferenceABC):
    def __init__(self):
        self.models: dict[str, list] = {"detection": [], "segmentation": []}

    def init(self) -> None:
        for model_name in consts.DetectionModels:
            model_path = self.get_model_path(model_name=model_name.value)
            tf_model = tf.keras.models.load_model(model_path)

            model_module = import_module(f"api.model.detection.{model_name.value}")
            model = model_module.model
            model.init("tensorflow")

            self.models["detection"].append(
                {"model_name": model_name, "tf_model": tf_model, "model": model}
            )

    def get_model_path(self, model_name: str) -> str:
        path = Path(
            f"{config.MODELS_FOLDER}",
            "tensorflow",
            f"{config.ML_HARDWARE}",
            f"{model_name}",
            f"{model_name}.h5",
        )
        return str(path)

    async def detection(self, model_name: str, image: Image) -> list:
        model, tf_model = next(
            (i["model"], i["tf_model"])
            for i in self.models["detection"]
            if i["model_name"] == model_name
        )
        model_input = model.set_model_input(image)
        model_output = tf_model.predict(model_input)
        predictions = model.decode_output(model_output, image)

        return predictions
