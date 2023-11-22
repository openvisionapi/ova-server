import sys

from api.config.api.config import config

if config.ML_FRAMEWORK == "tensorflow_lite":
    from api.inference.tensorflow_lite import TensorflowLiteInference as Inference

elif config.ML_FRAMEWORK == "tensorflow":
    from api.inference.tensorflow import TensorflowInference as Inference  # type: ignore

else:
    sys.exit(f"Unknow Framework `{config.ML_FRAMEWORK}`")

inference = Inference()
