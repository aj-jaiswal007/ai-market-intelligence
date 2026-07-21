from app.common.singleton import Singleton
from app.config.settings import get_settings
from tavily import TavilyClient
from typing import Any


class Tavily(metaclass=Singleton):
	def __init__(self):
		settings = get_settings()
		self.client = TavilyClient(settings.tavely_key)

	def search(self, query: str) -> dict[str, Any]:
		return self.client.search(query=query, search_depth="advanced")
