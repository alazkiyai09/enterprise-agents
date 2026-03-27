"""Compatibility helper for accessing the LangGraph workflow."""

from src.ad_insights.agents.insights_agent import AdInsightsAgent


def create_analysis_graph():
    return AdInsightsAgent().graph

