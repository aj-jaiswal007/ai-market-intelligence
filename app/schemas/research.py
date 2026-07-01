from pydantic import BaseModel

class ResearchRequest(BaseModel):
    market: str
    objective: str


class Competitors(BaseModel):
    name: str
    website: str
    description: str
    target_customers: list[str]
    pricing_model: str | None
    features: list[str]
    recent_news: list[str]
    sources: list[str]

class ResearchResult(BaseModel):
    competitors: list[Competitors]