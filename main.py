from fastapi import FastAPI
from app.api.routes.health import health_router

app = FastAPI(title="AI Market intelligence Platform Service", version="0.1.0")

app.include_router(health_router)
