import os


class Config:
    ML_FRAMEWORK = os.getenv("ML_FRAMEWORK", "tensorflow_lite")
    ML_HARDWARE = os.getenv("ML_HARDWARE", "cpu")

    MODELS_FOLDER = os.getenv("MODELS_FOLDER", "models")

    DETECTION_MODELS = ["yolov4"]

    # max size of 4MB
    MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", 4 * 1024 * 1024))

    DETECTION_RATE_LIMIT = os.getenv("DETECTION_RATE_LIMIT")


config = Config()
