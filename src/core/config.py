from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_name: str = 'Production Control API'
    app_debug: bool = False

    database_url: str
    redis_url: str = 'redis://localhost:6379/0'

    celery_broker_url: str
    celery_result_backend: str

    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_secure: bool = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()