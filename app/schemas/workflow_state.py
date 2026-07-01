from pydantic import BaseModel
from app.schemas.research import ResearchRequest, ResearchResult
from app.schemas.analysis import MarketAnalysis
from app.schemas.fact_check import FastCheckResult
from app.schemas.critic import CriticResult
from app.schemas.writer import FinalReport


class WorkflowState(BaseModel):
    request: ResearchRequest
    research: ResearchResult
    analysis: MarketAnalysis
    fact_check: FastCheckResult
    critic: CriticResult
    report: FinalReport
