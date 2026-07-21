from bs4 import BeautifulSoup
import aiohttp
from langchain_core.tools import tool
import logging

logger = logging.getLogger(__name__)


@tool
async def scrape_webpage(url: str) -> str:
	"""Fetches the webpage content and returns a clean text for the page

	Args:
	    url (str): URL to fetch

	Returns:
	    str: Webpage content
	"""
	logger.info(f"Fetching content for url: {url}")
	async with aiohttp.ClientSession() as session:
		async with session.get(url, ssl=False) as response:
			response = await response.text()

	soup = BeautifulSoup(response, "html.parser")
	# 1. Isolate the body element
	body = soup.find("body")

	# 2. Remove boilerplate/extraneous tags that AI doesn't need
	for element in body(["script", "style", "nav", "footer", "header"]):
		element.decompose()

	# 3. Extract the clean text
	return body.get_text(separator="\n", strip=True)
