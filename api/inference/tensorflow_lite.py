from importlib import import_module
from pathlib import Path

import tensorflow.lite as tflite
from PIL import Image

from api.config.api.config import config
from api.inference.base import InferenceABC


class TensorflowLiteInference(InferenceABC):
    def __init__(self):
        self.interpreters = {"detection": [], "segmentation": []}

    def init(self) -> None:
        for model_name in config.DETECTION_MODELS:
            model_path = self.get_model_path(model_name=model_name)
            if config.ML_HARDWARE == "edgetpu":
                interpreter = tflite.Interpreter(
                    model_path=model_path,
                    experimental_delegates=[tflite.load_delegate("libedgetpu.so.1")],
                )
            else:
                interpreter = tflite.Interpreter(model_path=model_path)

            interpreter.allocate_tensors()

            model_module = import_module(f"api.model.detection.{model_name}")
            model = model_module.model  # type: ignore
            model.init("tensorflow_lite")

            self.interpreters["detection"].append(
                {"model_name": model_name, "interpreter": interpreter, "model": model}
            )

    def get_model_path(self, model_name: str) -> str:
        path = Path(
            f"{config.MODELS_FOLDER}",
            "tensorflow_lite",
            f"{config.ML_HARDWARE}",
            f"{model_name}",
            f"{model_name}.tflite",
        )
        return str(path)

    def detection(self, model_name: str, image: Image) -> list:
        model, interpreter = next(
            (i["model"], i["interpreter"])
            for i in self.interpreters["detection"]
            if i["model_name"] == model_name
        )

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter_input = model.set_model_input(image)
        interpreter.set_tensor(input_details[0]["index"], interpreter_input)

        interpreter.invoke()

        model_output = interpreter.get_tensor(output_details[0]["index"])
        predictions = model.decode_output(model_output, image)

        return predictions
