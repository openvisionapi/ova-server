from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address

from api.inference import inference

limiter = Limiter(key_func=get_remote_address)


def init_api() -> FastAPI:
    server = FastAPI()
    server.state.limiter = limiter

    inference.init()

    @server.get("/health", status_code=200)
    async def health():
        return {"status": "OK"}

    from api.detection import routes
    from api.errors import handle_errors

    server.include_router(routes.router)

    handle_errors(server)

    return server
