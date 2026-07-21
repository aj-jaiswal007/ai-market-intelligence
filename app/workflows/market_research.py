from langgraph.graph import StateGraph, START, END
from app.schemas.workflow_state import WorkflowState
from app.nodes.researcher import ResearchNode


class MarketResearchWorkflow:
	def __init__(self):
		graph = StateGraph(WorkflowState)

		# Add Nodes
		graph.add_node("research", ResearchNode().execute)

		# Add edges
		graph.add_edge(START, "research")
		graph.add_edge("research", END)

		self.graph = graph.compile()
