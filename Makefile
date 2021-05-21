SHELL := /bin/bash

setup-tensorflow:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/tensorflow.txt \
	)

setup-tensorflow-lite:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/tensorflow_lite.txt \
	)

test:
	@(\
	    source .venv/bin/activate && \
	    flake8 && \
	    mypy api && \
	    bandit api && \
	    pycodestyle api && \
	    ML_FRAMEWORK=tensorflow pytest && \
	    ML_FRAMEWORK=tensorflow_lite pytest \
	)

dev:
	@(\
	    git clone https://github.com/openvisionapi/test-models.git testdata/test-models && \
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/dev.txt && \
	    pip3 install -r requirements/test.txt && \
	    pip3 install -r requirements/tensorflow.txt && \
	    pip3 install -r requirements/tensorflow_lite.txt \
	)

run:
	@(\
	    source .venv/bin/activate && \
	    gunicorn --reload --timeout=3000 --access-logfile=- server:server \
	)

pip-update:
	@(\
	    source .venv/bin/activate && \
	    pip-compile --output-file=requirements/common.txt -U requirements/common.in && \
	    pip-compile --output-file=requirements/dev.txt -U requirements/dev.in && \
	    pip-compile --output-file=requirements/test.txt -U requirements/test.in && \
	    pip-compile --output-file=requirements/tensorflow_lite.txt -U requirements/tensorflow_lite.in && \
	    pip-compile --output-file=requirements/tensorflow.txt -U requirements/tensorflow.in \
	)
