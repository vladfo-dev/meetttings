import logging
from fastapi import FastAPI
from backend.config import (
    DEBUG,
    PROJECT_NAME,
    VERSION,
)
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes import router_ready
log = logging.getLogger(__name__)


def get_app():
    """
        Initialize FastAPI application.
    Returns:
        app (FastAPI): Application object instance.
    """
    log.debug("Initialize FastAPI application node.")

    app = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version=VERSION,
        docs_url="/swagger",
    )

    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    log.debug("Add application routes.")
    app.include_router(router_ready)
    return app


application = get_app()