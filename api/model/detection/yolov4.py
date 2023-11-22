from pathlib import Path

import numpy as np
from PIL.Image import Image

from api.config.api.config import config as api_config
from api.config.detection.yolov4 import config as yolov4_config
from api.model.detection.utils import non_maximum_suppression


class Yolov4:
    def __init__(self):
        self.iou_threshold = yolov4_config.IOU_THRESHOLD
        self.input_size = yolov4_config.INPUT_SIZE
        self.labels = {}

    def init(self, ml_framework: str) -> None:
        labels_file_path = Path(
            f"{api_config.MODELS_FOLDER}",
            f"{ml_framework}",
            f"{api_config.ML_HARDWARE}",
            "yolov4",
            "labels.txt",
        )

        labels = {}
        with open(labels_file_path, "r") as f:
            for i, label in enumerate(f.read().splitlines()):
                labels[i] = label

        self.labels = labels

    def set_model_input(self, image: Image) -> np.ndarray:
        input_image = image.convert("RGB")
        input_image = input_image.resize(self.input_size)
        input_image = np.asanyarray(input_image)
        input_image = input_image / 255.0
        input_image = np.array(input_image).astype(np.float32)
        model_input = np.expand_dims(input_image, axis=0)
        return model_input

    def decode_output(self, model_output: np.ndarray, original_image: Image) -> list:
        boxes = model_output[:, :, 0:4]
        boxes = boxes[0]

        scores = model_output[:, :, 4:]
        scores = scores[0]

        nmsed_boxes, nmsed_scores, nmsed_classes = non_maximum_suppression(
            boxes=boxes, scores=scores, iou_threshold=self.iou_threshold
        )

        w, h = original_image.size
        pred_bboxes = []
        for boxe in nmsed_boxes:
            x1 = int(w * boxe[1])
            y1 = int(h * boxe[0])
            x2 = int(w * boxe[3])
            y2 = int(h * boxe[2])
            pred_bboxes.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

        pred_scores = list(map(lambda i: f"{i:.2f}", nmsed_scores))
        pred_labels = list(map(lambda i: self.labels[i], nmsed_classes))

        predictions = []
        for i in range(len(pred_labels)):
            predictions.append(
                {
                    "label": pred_labels[i],
                    "score": pred_scores[i],
                    "bbox": pred_bboxes[i],
                }
            )
        return predictions


model = Yolov4()
