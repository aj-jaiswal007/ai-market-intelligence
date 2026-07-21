from app.nodes.base import BaseNode
from app.schemas.workflow_state import WorkflowState
from app.services.research_service import ResearchService


class ResearchNode(BaseNode):
	"""Orchestrates the research step of the workflow"""

	def __init__(self, research_service: ResearchService | None = None):
		self.service = research_service or ResearchService()

	async def execute(self, state: WorkflowState) -> WorkflowState:
		result = await self.service.run(state)
		state.research = result
		return state
