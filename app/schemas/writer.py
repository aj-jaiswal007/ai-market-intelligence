from pydantic import BaseModel
from typing import Literal


class ReportSection(BaseModel):
	title: str
	markdown: str


class FinalReport(BaseModel):
	title: str
	summary: str
	sections: list[ReportSection]
