from abc import ABC
from pydantic import BaseModel


class SearchResult(BaseModel):
    url: str
    title: str
    description: str
    score: float


class SearchResponse(BaseModel):
    results: list[SearchResult]


class SearchClient(ABC):

    def search(self, query: str) -> SearchResponse: ...
