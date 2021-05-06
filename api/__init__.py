from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from api.config.api.config import config
from api.inference import inference  # type: ignore

limiter = Limiter(key_func=get_remote_address)


def init_api() -> Flask:
    server = Flask(__name__)
    server.config.from_object(config)

    inference.init()
    limiter.init_app(server)

    from api.detection.routes import detection
    from api.errors import errors
    from api.health import health

    server.register_blueprint(health)
    server.register_blueprint(errors)
    server.register_blueprint(detection)

    return server
