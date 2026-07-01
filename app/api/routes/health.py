from fastapi import APIRouter
from pydantic import BaseModel


class ReadyResponse(BaseModel):
    status: str

health_router = APIRouter(prefix="/health")


@health_router.get("/ready")
def ready() -> ReadyResponse:
    return ReadyResponse(status="OK")