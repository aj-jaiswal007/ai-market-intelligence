from langchain_core.tools import tool
from app.search.base import SearchResponse
from app.search.search_client_factory import SearchClientFactory
import logging

logger = logging.getLogger(__name__)


@tool
async def search_web(query: str) -> SearchResponse:
	"""Searches the web for the given query and returns the results.

	Args:
	    query (str): User query for the search.

	Returns:
	    SearchResponse: Response with search items.
	"""
	logger.info(f"Searching web for query: {query}")
	response = SearchClientFactory.get_client().search(query)
	logger.info(f"Got {len(response.results)} responses")
	return response
