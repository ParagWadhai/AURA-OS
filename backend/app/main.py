from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.api.v1.api import router

configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    debug=settings.DEBUG,
)


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "message": "Welcome to AURA-OS",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.APP_ENV,
    }

app.include_router(
    router,
    prefix=settings.API_V1_PREFIX,
)