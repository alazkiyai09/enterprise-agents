"""Compatibility alias for older AdInsights imports."""

from src.ad_insights.agents.insights_agent import AdInsightsAgent

AnalysisState = dict

__all__ = ["AdInsightsAgent", "AnalysisState"]

