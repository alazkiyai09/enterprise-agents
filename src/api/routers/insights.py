from uuid import uuid4

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/agents/insights", tags=["insights"])


class InsightsRequest(BaseModel):
    request: str = Field(..., min_length=1)
    campaign_id: str | None = None


def _get_agent(request: Request):
    from src.agents.insights.agent import AdInsightsAgent

    agent = getattr(request.app.state, "insights_agent", None)
    if agent is None:
        agent = AdInsightsAgent()
        request.app.state.insights_agent = agent
    return agent


@router.post("/analyze")
async def analyze(payload: InsightsRequest, request: Request) -> dict[str, object]:
    job_id = str(uuid4())
    result = _get_agent(request).analyze(payload.request, campaign_id=payload.campaign_id)
    request.app.state.insight_jobs[job_id] = result
    return {"job_id": job_id, "result": result}


@router.get("/{job_id}")
async def get_result(job_id: str, request: Request) -> dict[str, object]:
    result = request.app.state.insight_jobs.get(job_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "result": result}


@router.get("/quick-insights")
async def quick_insights(request: Request) -> dict[str, object]:
    return {"count": len(request.app.state.insight_jobs), "job_ids": list(request.app.state.insight_jobs)}


@router.post("/compare")
async def compare(payload: dict[str, object]) -> dict[str, object]:
    return {"status": "accepted", "comparison_request": payload}


@router.get("/benchmarks")
async def benchmarks() -> dict[str, object]:
    return {"status": "available", "providers": ["google_ads", "meta_ads", "tiktok_ads", "linkedin_ads"]}
