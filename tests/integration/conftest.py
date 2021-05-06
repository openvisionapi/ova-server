import pytest

from api import init_api
from api.config.api.config import config


@pytest.fixture
def app(monkeypatch):
    monkeypatch.setattr(config, "MODELS_FOLDER", "testdata/test-models/models")
    monkeypatch.setattr(config, "ML_HARDWARE", "cpu")
    app = init_api()
    yield app


@pytest.fixture
def test_client(app):
    yield app.test_client()
