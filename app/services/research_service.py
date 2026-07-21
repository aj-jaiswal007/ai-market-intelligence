from langchain.messages import HumanMessage, SystemMessage
from app.common.singleton import Singleton
from langchain.agents import create_agent
from app.tools.search import search_web
from app.tools.scraper import scrape_content
from langchain_google_genai import ChatGoogleGenerativeAI
from app.schemas.workflow_state import WorkflowState, ResearchResult
from app.config.settings import AppSettings, get_settings
from langchain.agents.middleware.tool_call_limit import ToolCallLimitMiddleware
import logging

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = SystemMessage(
	"""You are a market research analyst. Your task is ONLY to gather factual information.
Search for competitors in the given market using the following tools provided.

Workflow (must follow):

1. Call search_web exactly once to discover competitors.
2. Select the top 3 most relevant search result.
3. Call scrape_content for EACH search result URL.
4. Base your findings only on scraped content.
5. Do not produce the final answer until all scraping is complete.

Never rely only on search snippets.
"""
)


class ResearchService(metaclass=Singleton):
	def __init__(self, settings: AppSettings | None = None):

		settings = settings or get_settings()

		model = ChatGoogleGenerativeAI(
			model=settings.gemini_chat_model,
			api_key=settings.gemini_api_key,
		)
		limiter = ToolCallLimitMiddleware(tool_name="search_web", run_limit=1, thread_limit=2)

		self.agent = create_agent(
			model=model,
			tools=[search_web, scrape_content],
			system_prompt=SYSTEM_PROMPT,
			response_format=ResearchResult,
			middleware=[limiter],
		)

	async def run(self, state: WorkflowState) -> ResearchResult:
		result = await self.agent.ainvoke(
			{"messages": [HumanMessage(f"Market: {state.request.market}; Objective: {state.request.objective}")]}
		)
		logger.info(f"AI Response: {result}")
		return result["structured_response"]
