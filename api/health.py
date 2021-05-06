from flask import Blueprint

from api.utils import response

health = Blueprint("health", __name__)


@health.route("/health")
def check_health():
    return response({"status": "OK"}, 200)
