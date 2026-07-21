from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
	market: str
	objective: str


class Competitors(BaseModel):
	name: str = Field(..., description="name of the company")
	website: str = Field(..., description="website url of the company")
	description: str = Field(..., description="company description")
	target_customers: list[str] = Field(..., description="types of customers this company targets")
	pricing_model: str | None = Field(..., description="pricing model")
	features: list[str] = Field(..., description="company features")
	recent_news: list[str] = Field(..., description="any recent news of the company which can be considered alarming")
	sources: list[str] = Field(..., description="sources of the information")


class ResearchResult(BaseModel):
	competitors: list[Competitors] = Field(..., description="list of competitors")
