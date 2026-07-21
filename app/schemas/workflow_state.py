from pydantic import BaseModel
from app.schemas.research import ResearchRequest, ResearchResult
from app.schemas.analysis import MarketAnalysis
from app.schemas.fact_check import FastCheckResult
from app.schemas.critic import CriticResult
from app.schemas.writer import FinalReport


class WorkflowState(BaseModel):
	request: ResearchRequest
	research: ResearchResult | None = None
	analysis: MarketAnalysis | None = None
	fact_check: FastCheckResult | None = None
	critic: CriticResult | None = None
	report: FinalReport | None = None
