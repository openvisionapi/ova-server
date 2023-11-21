default:
    @just --list

#
# Tensorflow
#

setup-tensorflow:
    #!/usr/bin/env bash
    poetry install --only main,tensorflow,dev

run-with-tensorflow:
    #!/usr/bin/env bash
    ML_FRAMEWORK=tensorflow poetry run uvicorn --reload  --access-log  server:server

#
# Tensorflow lite
#

setup-tensorflow-lite:
    #!/usr/bin/env bash
    poetry install --only main,tensorflow_lite,dev

run-with-tensorflow-lite:
    #!/usr/bin/env bash
    poetry run uvicorn --access-log server:server

update:
    #!/usr/bin/env bash
    poetry update

dev:
    #!/usr/bin/env bash
    if [ ! -d "testdata" ]; then
        git clone https://github.com/openvisionapi/test-models.git testdata/test-models
    fi
    poetry install

test:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    mypy api &&
    bandit api &&
    ML_FRAMEWORK=tensorflow pytest tests &&
    ML_FRAMEWORK=tensorflow_lite pytest tests
