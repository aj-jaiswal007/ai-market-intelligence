from abc import ABC, abstractmethod
from app.schemas.workflow_state import WorkflowState


class BaseNode(ABC):

    async def execute(self, state: WorkflowState) -> WorkflowState: ...
