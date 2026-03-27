from datetime import datetime, timezone

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/agents/support", tags=["support"])


class SupportChatRequest(BaseModel):
    user_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class FeedbackRequest(BaseModel):
    user_id: str
    session_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = None


@router.post("/chat")
async def chat(payload: SupportChatRequest) -> dict[str, object]:
    from src.agents.support.agent import get_support_agent

    response = get_support_agent().chat(user_id=payload.user_id, message=payload.message)
    return {
        "message": response.message,
        "intent": response.intent,
        "sentiment": response.sentiment.label,
        "ticket_created": response.ticket_created,
        "escalated": response.escalated,
        "sources": response.sources,
    }


@router.websocket("/ws/{user_id}")
async def websocket_chat(websocket: WebSocket, user_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            message = str(data.get("message") or data.get("content") or "").strip()
            if not message:
                await websocket.send_json({"type": "error", "error": "message is required"})
                continue
            from src.agents.support.agent import get_support_agent

            response = get_support_agent().chat(user_id=user_id, message=message)
            await websocket.send_json(
                {
                    "type": "response",
                    "message": response.message,
                    "intent": response.intent,
                    "sentiment": response.sentiment.label,
                    "ticket_created": response.ticket_created,
                    "escalated": response.escalated,
                }
            )
    except WebSocketDisconnect:
        return


@router.post("/tickets")
async def create_ticket(payload: SupportChatRequest) -> dict[str, object]:
    from src.agents.support.agent import get_support_agent

    response = get_support_agent().chat(user_id=payload.user_id, message=payload.message)
    return {
        "status": "processed",
        "ticket_created": response.ticket_created,
        "escalated": response.escalated,
    }


@router.get("/tickets/{user_id}")
async def get_tickets(user_id: str) -> dict[str, object]:
    from src.agents.support.tools import get_ticket_store

    tickets = [ticket.to_dict() for ticket in get_ticket_store().get_user_tickets(user_id)]
    return {"user_id": user_id, "count": len(tickets), "tickets": tickets}


@router.get("/conversation/{id}")
async def get_conversation(id: str) -> dict[str, object]:
    from src.agents.support.agent import get_support_agent

    messages = get_support_agent().get_conversation_history(id)
    return {"user_id": id, "count": len(messages), "messages": messages}


@router.post("/feedback")
async def feedback(payload: FeedbackRequest) -> dict[str, object]:
    return {
        "status": "accepted",
        "user_id": payload.user_id,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
