import os

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/agents/fraud", tags=["fraud"])


class FraudAlertRequest(BaseModel):
    alert_id: str = Field(..., min_length=1)
    alert_type: str = Field(..., min_length=1)
    transaction_amount: float = Field(..., gt=0)
    customer_id: str = Field(..., min_length=1)


class ManualReviewRequest(BaseModel):
    reviewer: str = Field(..., min_length=1)
    notes: str = Field(..., min_length=1)


def _get_agent(request: Request):
    from src.agents.fraud.agent import FraudTriageAgent

    agent = getattr(request.app.state, "fraud_agent", None)
    if agent is None:
        environment = os.getenv("ENVIRONMENT")
        if not environment:
            environment = "demo" if os.getenv("GLM_API_KEY") else "development"
        agent = FraudTriageAgent(environment=environment)
        request.app.state.fraud_agent = agent
    return agent


@router.post("/alerts")
async def submit_alert(payload: FraudAlertRequest, request: Request) -> dict[str, object]:
    agent = _get_agent(request)
    try:
        result = await agent.arun(
            alert_id=payload.alert_id,
            alert_type=payload.alert_type,
            transaction_amount=payload.transaction_amount,
            customer_id=payload.customer_id,
        )
    except ValueError:
        # Fallback for unknown upstream enum variants.
        result = await agent.arun(
            alert_id=payload.alert_id,
            alert_type="other",
            transaction_amount=payload.transaction_amount,
            customer_id=payload.customer_id,
        )
    request.app.state.fraud_alerts[payload.alert_id] = result
    return {"status": "completed", "alert_id": payload.alert_id, "result": result}


@router.get("/alerts/{id}")
async def get_alert(id: str, request: Request) -> dict[str, object]:
    alert = request.app.state.fraud_alerts.get(id)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"alert_id": id, "result": alert}


@router.get("/alerts")
async def list_alerts(request: Request) -> dict[str, object]:
    return {
        "count": len(request.app.state.fraud_alerts),
        "alerts": request.app.state.fraud_alerts,
    }


@router.post("/alerts/{id}/review")
async def manual_review(id: str, payload: ManualReviewRequest, request: Request) -> dict[str, object]:
    alert = request.app.state.fraud_alerts.get(id)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    alert["manual_review"] = {"reviewer": payload.reviewer, "notes": payload.notes}
    return {"status": "recorded", "alert_id": id}
