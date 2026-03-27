"""Structured data models for AdInsights exports and reports."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class MetricType(str, Enum):
    IMPRESSIONS = "impressions"
    CLICKS = "clicks"
    CTR = "ctr"
    CPC = "cpc"
    CONVERSIONS = "conversions"
    CPA = "cpa"
    ROAS = "roas"


class CampaignData(BaseModel):
    campaign_id: str
    campaign_name: str | None = None
    platform: str | None = None
    metrics: dict[str, Any] = Field(default_factory=dict)


class AnalysisConfig(BaseModel):
    include_anomalies: bool = True
    include_trends: bool = True
    include_benchmarks: bool = True
    include_charts: bool = True


class ReportConfig(BaseModel):
    title: str = "Ad Insights Report"
    output_format: str = "markdown"
    include_recommendations: bool = True


class AnalysisResult(BaseModel):
    success: bool = True
    report: str = ""
    insights: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    charts: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

