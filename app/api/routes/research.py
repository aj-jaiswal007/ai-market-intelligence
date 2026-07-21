from fastapi import APIRouter
from app.schemas.research import ResearchRequest, ResearchResult
from app.schemas.workflow_state import WorkflowState
from app.services.research_service import ResearchService


research_router = APIRouter(prefix="/research")


@research_router.post("/")
async def research(research_request: ResearchRequest) -> ResearchResult:

	research_service = ResearchService()
	return await research_service.run(state=WorkflowState(request=research_request))
