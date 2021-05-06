import numpy as np

# https://arxiv.org/pdf/1704.04503.pdf


def non_maximum_suppression(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float) -> tuple:
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    nmsed_boxes = []
    nmsed_scores = []
    nmsed_classes = []

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    highest_score_classes = np.argmax(scores, axis=1)
    scores = np.max(scores, axis=1)
    order = np.argsort(scores)

    while order.size > 0:
        index = order[-1]

        nmsed_boxes.append(boxes[index])
        nmsed_scores.append(scores[index])
        nmsed_classes.append(highest_score_classes[index])

        xx1 = np.maximum(x1[index], x1[order[:-1]])
        xx2 = np.minimum(x2[index], x2[order[:-1]])
        yy1 = np.maximum(y1[index], y1[order[:-1]])
        yy2 = np.minimum(y2[index], y2[order[:-1]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        intersection = w * h

        ratio = intersection / (areas[index] + areas[order[:-1]] - intersection)

        left = np.where(ratio < iou_threshold)
        order = order[left]

    return nmsed_boxes, nmsed_scores, nmsed_classes
