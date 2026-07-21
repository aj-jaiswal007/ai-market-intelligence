from langgraph.graph import StateGraph
from langchain.messages import HumanMessage, SystemMessage
from app.common.singleton import Singleton
from langchain.agents import create_agent
from app.tools.search import search_web
from app.tools.scraper import scrape_webpage
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from app.schemas.workflow_state import WorkflowState, ResearchResult
from app.config.settings import AppSettings, get_settings

SYSTEM_PROMPT = SystemMessage(
	"""You are a market research analyst. Your task is ONLY to gather factual information.
Search for competitors in the given market using the tools provided.
"""
)


class ResearchService(metaclass=Singleton):
	def __init__(self, settings: AppSettings | None = None):

		settings = settings or get_settings()

		model = ChatGoogleGenerativeAI(
			model=settings.gemini_chat_model,
			api_key=settings.gemini_api_key,
		)

		self.agent = create_agent(
			model=model,
			tools=[search_web, scrape_webpage],
			system_prompt=SYSTEM_PROMPT,
			response_format=ResearchResult,
		)

	async def run(self, state: WorkflowState) -> ResearchResult:
		return await self.agent.ainvoke(
			{"messages": [HumanMessage(f"Market: {state.request.market}; Objective: {state.request.objective}")]}
		)
