from flask import Blueprint

from api.utils import response

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(401)
def http_401(exception):
    message = {"description": "Unauthorized"}
    return response(message, 401)


@errors.app_errorhandler(404)
def http_404(exception):
    message = {"description": "Requested page not found"}
    return response(message, 404)


@errors.app_errorhandler(405)
def http_405(exception):
    message = {"description": "Method Not allowed"}
    return response(message, 405)


@errors.app_errorhandler(422)
def http_422(exception):
    message = {
        "description": "Unprocessable entity",
        "content": {"message": exception.exc.messages},
    }
    return response(message, 422)


@errors.app_errorhandler(500)
def http_500(exception):
    message = {"description": "Internal server error"}
    return response(message, 500)
