from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from api import exceptions


def handle_errors(app):
    @app.exception_handler(exceptions.ImageTooLarge)
    async def image_too_large(request, exception):
        return JSONResponse(status_code=413, content={"error": str(exception)})

    @app.exception_handler(exceptions.UnsupportedImageType)
    async def unsupported_image_type(request, exception):
        return JSONResponse(status_code=415, content={"error": str(exception)})

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit(request, exception):
        return JSONResponse(
            status_code=429,
            content={
                "error": f"Too many requests: the limit is {str(exception.detail)}"
            },
        )
