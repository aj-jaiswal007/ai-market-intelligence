from pydantic_settings import BaseSettings
from app.enums.environment import Environment
from functools import lru_cache
from app.enums.search_provider import SearchProvider


class AppSettings(BaseSettings):
    environment: Environment = Environment.LOCAL

    search_provider: SearchProvider = SearchProvider.TAVILY

    travely_key: str = ""


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
