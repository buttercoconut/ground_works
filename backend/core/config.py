"""Configuration for the Ground Works backend.

Environment variables are loaded via Pydantic's BaseSettings.  The
configuration is intentionally minimal – only the database URL is required.
"""

from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
