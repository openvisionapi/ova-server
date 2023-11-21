import pytest
from httpx import AsyncClient


from api import init_api
from api.config.api.config import config


@pytest.fixture
async def api(monkeypatch):
    monkeypatch.setattr(config, "MODELS_FOLDER", "testdata/test-models/models")
    monkeypatch.setattr(config, "ML_HARDWARE", "cpu")
    api = init_api()
    yield AsyncClient(
        app=api,
        base_url="http://test/",
    )
