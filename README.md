<div align="center">

# 🤖 Enterprise Agents

### Support Agent • Fraud Triage • Ad Insights • LLMOps Evaluation

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-FF6B6B?style=flat)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-0C4C97?style=flat&logo=langchain)](https://www.langchain.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus)](https://prometheus.io/)

[Overview](#-overview) • [About](#-about) • [Topics](#-topics) • [API](#-api-surfaces) • [Quick Start](#-quick-start)

---

Multi-agent orchestration platform for enterprise workflows with **customer support automation**, **fraud investigation**, **marketing insights**, and **LLM quality evaluation** under a single API surface.

</div>

---

## 🎯 Overview

`enterprise-agents` unifies three agent products and one evaluation layer:

- Support conversations with memory and ticketing
- Fraud triage pipelines with risk decisions
- Ad campaign analytics and benchmark comparisons
- LLMOps evaluation, metrics, and report workflows

## 📌 About

- Single backend for operational AI agents and quality controls
- Built for observability, structured routing, and modular expansion
- Supports real-time and API-driven interaction patterns

## 🏷️ Topics

`enterprise-agents` `langgraph` `ai-agents` `fraud-detection` `customer-support-ai` `ad-analytics` `llmops` `evaluation` `fastapi`

## 🧩 Architecture

- `src/api/`: unified FastAPI app and routers
- `src/agents/`: support, fraud, and insights agent modules
- `src/evaluation/`: metrics, datasets, and eval runners
- `src/memory/`: conversation memory management
- `src/monitoring/`: observability instrumentation
- `src/core/`: auth, security, rate limiting, errors, secrets

## 🌐 API Surfaces

- `POST /api/v1/agents/support/chat`
- `POST /api/v1/agents/support/tickets`
- `GET /api/v1/agents/support/tickets/{user_id}`
- `POST /api/v1/agents/fraud/alerts`
- `GET /api/v1/agents/fraud/alerts/{id}`
- `POST /api/v1/agents/insights/analyze`
- `GET /api/v1/agents/insights/quick-insights`
- `POST /api/v1/eval/run`
- `GET /api/v1/eval/metrics`
- `GET /health`

## ⚡ Quick Start

```bash
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

## 🔧 GLM Setup

```bash
export GLM_API_KEY=your_glm_api_key
export GLM_BASE_URL=https://api.z.ai/api/anthropic
export GLM_MODEL=glm-5.1

export LLM_PROVIDER=anthropic
export LLM_BASE_URL=https://api.z.ai/api/anthropic
export LLM_MODEL_NAME=glm-5.1
export OPENAI_API_KEY=$GLM_API_KEY

export ENVIRONMENT=demo
export ZHIPUAI_API_KEY=$GLM_API_KEY
```

## 🛠️ Tech Stack

**Core:** FastAPI, Pydantic, Uvicorn  
**Agents:** LangGraph, LangChain  
**Storage:** SQLite, ChromaDB  
**Monitoring:** Prometheus, metrics pipelines
