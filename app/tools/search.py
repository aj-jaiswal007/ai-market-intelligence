import aiohttp
from langchain_core.tools import tool
from app.search.base import SearchResponse
from app.search.search_client_factory import SearchClientFactory


async def search_web(query: str) -> SearchResponse:
    """Searches the web for the given query and returns the results.

    Args:
        query (str): User query for the search.

    Returns:
        SearchResponse: Response with search items.
    """
    return SearchClientFactory.get_client().search(query)
