from abc import ABC
from pydantic import BaseModel, Field


class SearchResult(BaseModel):
	url: str = Field(..., description="web url of the search result")
	title: str = Field(..., description="title of the search result")
	content: str = Field(..., description="brief content of the result")
	score: float = Field(..., description="matching score against the search query")


class SearchResponse(BaseModel):
	results: list[SearchResult] = Field(..., description="list of SearchResult objects")

	def format_results(self) -> str:
		lines = ["Results:"]
		for i, result in enumerate(self.results):
			content = f"{i + 1}.\n URL: {result.url}\n Title: {result.title}\n Content: {result.content}\n Score: {result.score}\n\n\n"
			lines.append(content)

		return "\n".join(lines)


class SearchClient(ABC):
	def search(self, query: str) -> SearchResponse: ...
