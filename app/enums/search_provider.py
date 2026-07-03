from enum import Enum


class SearchProvider(str, Enum):
    TAVILY = "TAVILY"
    FIRECRAWL = "FIRECRAWL"
