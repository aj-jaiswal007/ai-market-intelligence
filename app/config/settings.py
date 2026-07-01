from pydantic_settings import BaseSettings
from app.enums.environment import Environment
from functools import lru_cache

class AppSettings(BaseSettings):
    environment: Environment = Environment.LOCAL

@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
