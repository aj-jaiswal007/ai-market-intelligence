from pydantic import BaseModel


class SWOT(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    opportunities: list[str]
    threats: list[str]


class CompetitorAnalysis(BaseModel):
    competitor: str
    swot: SWOT
    positioning: str


class MarketAnalysis(BaseModel):
    trends: list[str]
    opportunities: list[str]
    risks: list[str]
    competitors: list[CompetitorAnalysis]
