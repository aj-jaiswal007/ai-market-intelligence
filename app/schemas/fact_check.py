from pydantic import BaseModel
from typing import Literal


class VerifiedClaim(BaseModel):
	statement: str
	status: Literal["verified", "unsupported", "contradicted"]
	evidence: list[str]


class FastCheckResult(BaseModel):
	claims: list[VerifiedClaim]
