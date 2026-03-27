from fastapi import FastAPI

from src.api.routers.evaluation import router as evaluation_router
from src.api.routers.fraud import router as fraud_router
from src.api.routers.insights import router as insights_router
from src.api.routers.support import router as support_router

app = FastAPI(
    title="enterprise-agents",
    version="0.1.0",
    description="Unified agent platform shell for support, fraud triage, insights, and evaluation.",
)

app.state.fraud_alerts = {}
app.state.insight_jobs = {}
app.state.evaluations = {}
app.state.datasets = {}

app.include_router(support_router)
app.include_router(fraud_router)
app.include_router(insights_router)
app.include_router(evaluation_router)


@app.get("/health", tags=["system"])
async def health() -> dict[str, object]:
    return {
        "status": "healthy",
        "repo": "enterprise-agents",
        "alert_count": len(app.state.fraud_alerts),
        "insight_jobs": len(app.state.insight_jobs),
        "evaluations": len(app.state.evaluations),
    }


@app.get("/metrics", tags=["system"])
async def metrics() -> dict[str, object]:
    return {
        "repo": "enterprise-agents",
        "support_enabled": True,
        "fraud_alerts": len(app.state.fraud_alerts),
        "insight_jobs": len(app.state.insight_jobs),
        "evaluations": len(app.state.evaluations),
    }
