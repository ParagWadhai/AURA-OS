from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # model_config = SettingsConfigDict(
    #     env_file=".env",
    #     extra="ignore",
    # )
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

    # ---------------------------------------------------
    # Application
    # ---------------------------------------------------
    APP_NAME: str = "AURA-OS"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    # ---------------------------------------------------
    # FastAPI
    # ---------------------------------------------------
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # ---------------------------------------------------
    # PostgreSQL
    # ---------------------------------------------------
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # ---------------------------------------------------
    # Redis
    # ---------------------------------------------------
    REDIS_HOST: str
    REDIS_PORT: int

    # ---------------------------------------------------
    # Chroma
    # ---------------------------------------------------
    CHROMA_HOST: str
    CHROMA_PORT: int

    # ---------------------------------------------------
    # JWT
    # ---------------------------------------------------
    JWT_SECRET_KEY: str = Field(...)

    JWT_ALGORITHM: str = "HS256"

    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ---------------------------------------------------
    # Embeddings
    # ---------------------------------------------------
    EMBEDDING_MODEL: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()