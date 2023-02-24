default:
    @just --list

#
# Tensorflow
#

setup-tensorflow:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/tensorflow.txt

run-with-tensorflow:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    ML_FRAMEWORK=tensorflow gunicorn --reload --timeout=3000 --access-logfile - --error-logfile - server:server

run-with-tensorflow-lite:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    gunicorn --reload --timeout=3000 --access-logfile - --error-logfile - server:server

# build-for-tensorflow:
#     buildah build -f Containerfile.tensorflow -t openvisionapi:tensorflow .
#
# deploy-tensorflow-version:
#     podman run -d openvisionapi:tensorflow
#
# Dev and Test
#

pip-update:
    #!/usr/bin/env bash
    pip-compile --output-file=requirements/common.txt -U requirements/common.in --resolver=backtracking &&
    pip-compile --output-file=requirements/dev.txt -U requirements/dev.in --resolver=backtracking &&
    pip-compile --output-file=requirements/test.txt -U requirements/test.in --resolver=backtracking &&
    pip-compile --output-file=requirements/tensorflow.txt -U requirements/tensorflow.in --resolver=backtracking

dev:
    #!/usr/bin/env bash
    git clone https://github.com/openvisionapi/test-models.git testdata/test-models &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/dev.txt &&
    pip3 install -r requirements/test.txt &&
    pip3 install -r requirements/tensorflow.txt

test:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    flake8 &&
    mypy api &&
    bandit api &&
    pycodestyle api &&
    ML_FRAMEWORK=tensorflow pytest tests &&
    ML_FRAMEWORK=tensorflow_lite pytest tests
