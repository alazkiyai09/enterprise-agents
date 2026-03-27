"""
FastAPI application and models.
"""

from src.ad_insights.api.main import (
    app,
    get_agent,
    job_store,
    main,
    # Request/Response Models
    AnalysisRequest,
    AnalysisResponse,
    QuickInsightsRequest,
    QuickInsightsResponse,
    ComparisonRequest,
    ComparisonResponse,
    JobStatusResponse,
    BenchmarkResponse,
    HealthResponse,
)

__all__ = [
    # App
    "app",
    "main",
    # Utilities
    "get_agent",
    "job_store",
    # Models
    "AnalysisRequest",
    "AnalysisResponse",
    "QuickInsightsRequest",
    "QuickInsightsResponse",
    "ComparisonRequest",
    "ComparisonResponse",
    "JobStatusResponse",
    "BenchmarkResponse",
    "HealthResponse",
]

