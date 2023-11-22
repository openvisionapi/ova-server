<div align="center">
<p align="center">
  <img src="assets/ova.png" alt="Open Vision API"></img>
</p>

![Static Badge](https://img.shields.io/badge/AGPLV3-License?style=for-the-badge&label=LIcense)

</div>

## 🌟 Project Description

Open Vision API is an open source computer vision API that uses oepn source deep learning models for object detection.

<div align="center">
<img src="https://openvisionapi.com/images/demo.jpeg"  width="60%" height="30%">
</div>

<br>

## 🚀 Quick Start

The following instructions detail how to set up the ova-server.

For information regarding the official clients and a quick demo of the API functionality head to:

- [ova-client](https://github.com/openvisionapi/ova-client): the official Python client.
- [ova](https://github.com/openvisionapi/ova): the official Rust client.

### Installation

Make sure you have:

- [just](https://github.com/casey/just)
- [poetry](https://python-poetry.org/)

Set up a local environment using TensorFlow Lite as the backend framework.

```bash
$ just setup-tensorflow-lite
```

> See [documentation](https://openvisionapi-documentation.readthedocs.io/en/latest/) for a list of supported deep learning frameworks.

Download the models.

```bash
$ poetry run ./cli.py download --model=yolov4 --framework=tensorflow_lite --hardware=cpu
```

### Usage

Run the ova-server.

```bash
$ just run-with-tensorflow-lite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
INFO:     Started server process [3588600]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Get the official client.

#### Python client:

```bash
$ git clone https://github.com/openvisionapi/ova-client
$ cd ova-client
$ just setup
$ OVA_DETECTION_URL=http://localhost:8000/api/v1/detection poetry run ./ova.py detection images/cat.jpeg
```

> For more information about the python client, please visit https://github.com/openvisionapi/ova-client

#### Rust client:

```bash
$ git clone https://github.com/openvisionapi/ova
$ cd ova
$ OVA_DETECTION_URL=http://localhost:8000/api/v1/detection cargo run -- detection -i assets/cat.jpeg
```

> For more information about the rust client, please visit https://github.com/openvisionapi/ova

<br>

## ⛏️ Built Using

- [FastAPI](https://github.com/tiangolo/fastapi)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Numpy](https://github.com/numpy/numpy)
- [TensorFlow](https://github.com/tensorflow/tensorflow)
- [TensorFlow Lite](https://github.com/tensorflow/tensorflow)

<br>

## 🤝 Contributions

All contributions are welcome!

### Setting up the Development Environment

To set up the development environment, simply run the command:

```bash
$ just dev
```

### Code Style Checks

ruff and mypy are used to ensure that contributions are stylized in a uniform manner.

- [ruff](https://github.com/astral-sh/ruff) is used as a linter and a code formatter.
- [mypy](https://github.com/python/mypy) is used for static typing.

<br>

## 🔧 Tests

To run the tests, simply use the commands:

```bash
$ just dev
$ just test
```

<br>

## 📄 Documentation

The complete documentation can be found here [documentation](https://openvisionapi-documentation.readthedocs.io/en/latest/)

<br>

## ⚖️ License

AGPLv3
