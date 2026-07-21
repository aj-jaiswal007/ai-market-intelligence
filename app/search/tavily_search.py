from app.search.base import SearchClient, SearchResponse
from app.common.singleton import Singleton
from app.config.settings import get_settings
from tavily import TavilyClient


class TavilySearch(SearchClient, metaclass=Singleton):
	def __init__(self):
		settings = get_settings()
		self._client = TavilyClient(api_key=settings.tavely_key)

	def search(self, query: str) -> SearchResponse:
		response = self._client.search(query=query, search_depth="advanced")
		return SearchResponse.model_validate({"results": response["results"]})
