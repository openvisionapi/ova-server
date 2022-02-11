def test_detection_should_return_correct_predictions(test_client):
    url = "/api/v1/detection"
    data = {
        "model": "yolov4",
        "image": (open("testdata/detection/input_image.jpeg", "rb"), "test_image.jpeg"),
    }

    response = test_client.post(url, data=data)

    expected_json = {
        'description': 'Detected objects',
        'predictions': [
            {'bbox': {'x1': 451, 'x2': 987, 'y1': 91, 'y2': 1377}, 'label': 'cat', 'score': '0.42'}
        ],
    }

    assert response.status_code == 200
    assert response.json == expected_json
