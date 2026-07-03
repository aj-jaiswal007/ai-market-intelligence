from app.search.base import SearchClient
from app.search.tavily_search import TavilySearch
from app.config.settings import get_settings
from app.enums.search_provider import SearchProvider


class SearchClientFactory:

    @classmethod
    def get_client(cls) -> SearchClient:
        settings = get_settings()

        match settings.search_provider:
            case SearchProvider.TAVILY:
                return TavilySearch()
            case _:
                raise NotImplementedError(
                    f"{settings.search_provider} is not Implemented!"
                )
