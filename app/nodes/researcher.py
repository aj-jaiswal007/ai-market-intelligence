from app.nodes.base import BaseNode
from app.schemas.workflow_state import WorkflowState


class ResearchNode(BaseNode):
    """Orchestrates the research step of the workflow

    Args:
        BaseNode (_type_): _description_
    """

    def __init__(self, research_service):
        self.service = research_service

    async def execute(self, state: WorkflowState):
        result = await self.service.run(state)
        state.research = result
        return state
