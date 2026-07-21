from pydantic import BaseModel
from typing import Literal


class Issue(BaseModel):
	severity: Literal["low", "medium", "high"]
	issue: str
	recommendation: str


class CriticResult(BaseModel):
	score: int
	issues: list[Issue]
