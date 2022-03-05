<div align="center">

<p align="cetner">
  <img src="assets/ova.png" alt="Open Vision API"></img>
</p>

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

</div>

## 🚀 Quick start

Checkout [ova-client](https://github.com/openvisionapi/ova-client) for a quick demo.


### Installing
1. Setup a local enviroment using tensorflow lite as backend framework
```
$ make setup-tensorflow-lite
```
> See [the documentation](https://openvisionapi-documentation.readthedocs.io/en/latest/) for the list of supported deep learning frameworks.

2. Download the models:

```bash
$ source .venv/bin/activate
$ ./cli.py download --model=yolov4 --framework=tensorflow_lite --hardware=cpu
```

### Usage
Run the ova-server
```bash
$ make run

[2021-03-26 19:45:37 +0100] [396769] [INFO] Starting gunicorn 20.0.4
[2021-03-26 19:45:37 +0100] [396769] [INFO] Listening at: http://0.0.0.0:8000 (396769)
[2021-03-26 19:45:37 +0100] [396769] [INFO] Using worker: sync
[2021-03-26 19:45:37 +0100] [396771] [INFO] Booting worker with pid: 396771
```
Get the official client
```bash
$ git clone https://github.com/openvisionapi/ova-client
$ cd ova-client
$ make setup
$ source .venv/bin/activate
$ DETECTION_URL=http://localhost:8000/api/v1/detection ./ova_client.py detection images/cat.jpeg
```

> More information about the ova-client https://github.com/openvisionapi/ova-client

## ⛏️  Built Using
- [Flask](https://github.com/pallets/flask)
- [Marshmallow](https://github.com/marshmallow-code/marshmallow)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Numpy](https://github.com/numpy/numpy)
- [Tensorflow](https://github.com/tensorflow/tensorflow)
- [Tensorflow lite](https://github.com/tensorflow/tensorflow)

## ✍️  Author
[Badr BADRI](https://github.com/pythops)

## 🤝 Contributing
Your contributions are welcome !

### Setting up development environment
To setup the development environment, simply run this command
```
$ make dev
```
### Code-style checks
[black](https://github.com/psf/black) is used for code formatting.

[mypy](https://github.com/python/mypy) is used for static typing.

## 🔧 Tests
To run the tests, simply run those commands
```
$ make dev
$ make test
```

## 📄 Documentation
Full documentation can be found here:

https://openvisionapi-documentation.readthedocs.io/en/latest/

## ⚖️  License
AGPLv3

Copyright © 2021-2022 Badr BADRI @pythops
