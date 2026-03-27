from uuid import uuid4

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/eval", tags=["evaluation"])


class EvaluationRequest(BaseModel):
    name: str = Field(..., min_length=1)
    dataset: str = Field(..., min_length=1)


class DatasetUploadRequest(BaseModel):
    name: str = Field(..., min_length=1)
    records: list[dict[str, object]] = Field(default_factory=list)


class ModelCompareRequest(BaseModel):
    models: list[str] = Field(..., min_length=2)
    dataset: str = Field(..., min_length=1)


@router.post("/run")
async def run_evaluation(payload: EvaluationRequest, request: Request) -> dict[str, object]:
    eval_id = str(uuid4())
    request.app.state.evaluations[eval_id] = {
        "status": "accepted",
        "name": payload.name,
        "dataset": payload.dataset,
        "report_id": eval_id,
    }
    return {"eval_id": eval_id, "status": "accepted"}


@router.get("/{eval_id}")
async def get_evaluation(eval_id: str, request: Request) -> dict[str, object]:
    return request.app.state.evaluations.get(eval_id, {"status": "not_found"})


@router.post("/datasets/upload")
async def upload_dataset(payload: DatasetUploadRequest, request: Request) -> dict[str, object]:
    request.app.state.datasets[payload.name] = payload.records
    return {"status": "stored", "dataset": payload.name, "records": len(payload.records)}


@router.get("/datasets")
async def list_datasets(request: Request) -> dict[str, object]:
    return {
        "datasets": [
            {"name": name, "records": len(records)}
            for name, records in request.app.state.datasets.items()
        ]
    }


@router.post("/models/compare")
async def compare_models(payload: ModelCompareRequest) -> dict[str, object]:
    return {
        "status": "accepted",
        "models": payload.models,
        "dataset": payload.dataset,
    }


@router.get("/reports/{eval_id}")
async def get_report(eval_id: str, request: Request) -> dict[str, object]:
    evaluation = request.app.state.evaluations.get(eval_id)
    if evaluation is None:
        return {"status": "not_found"}
    return {
        "eval_id": eval_id,
        "report": f"Evaluation {evaluation['name']} for dataset {evaluation['dataset']} is queued.",
    }


@router.get("/metrics")
async def metrics() -> dict[str, object]:
    return {
        "metrics": [
            "accuracy",
            "similarity",
            "latency",
            "cost",
            "hallucination",
            "toxicity",
            "format",
            "exact",
            "custom",
        ]
    }


@router.get("/providers")
async def providers() -> dict[str, object]:
    return {"providers": ["openai", "anthropic", "cohere", "ollama", "glm"]}
