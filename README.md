# Enterprise AI Agents Platform (`enterprise-agents`)

Production-ready multi-agent platform for **customer support automation**, **fraud triage workflows**, **marketing/ad insights analytics**, and **LLM evaluation operations**. Built around a unified API to support enterprise orchestration and observability.

## Why This Repository

Modern teams need AI agents that can reason over business context, trigger operational actions, and be measured continuously. `enterprise-agents` centralizes these concerns in one maintainable codebase.

## Core Features

- Support agent orchestration with chat and ticket workflows
- Fraud triage endpoints for alert intake, review, and tracking
- Insights agent endpoints for analysis, comparisons, and benchmarks
- Evaluation module for datasets, model comparison, metrics, and reports
- Unified FastAPI application for all agent surfaces
- Core security/auth/rate-limit utilities in `src/core`

## Project Structure

- `src/api/`: unified API entrypoint and route modules
- `src/agents/`: support, fraud, and insights agent surfaces
- `src/evaluation/`: metrics, providers, and evaluation runners
- `src/memory/`: conversation memory support
- `src/monitoring/`: metrics and monitoring utilities
- `src/core/`: shared production concerns (auth, security, errors)

## API Endpoints

- `POST /api/v1/agents/support/chat`
- `POST /api/v1/agents/support/tickets`
- `GET /api/v1/agents/support/tickets/{user_id}`
- `GET /api/v1/agents/support/conversation/{id}`
- `POST /api/v1/agents/fraud/alerts`
- `GET /api/v1/agents/fraud/alerts/{id}`
- `POST /api/v1/agents/fraud/alerts/{id}/review`
- `POST /api/v1/agents/insights/analyze`
- `GET /api/v1/agents/insights/quick-insights`
- `POST /api/v1/eval/run`
- `GET /api/v1/eval/metrics`
- `GET /health`

## Quick Start

```bash
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

## GLM Configuration

Use the Anthropic-compatible GLM endpoint for support, fraud triage, and insights flows:

```bash
export GLM_API_KEY=your_glm_api_key
export GLM_BASE_URL=https://api.z.ai/api/anthropic
export GLM_MODEL=glm-5.1

# Support agent (ChatAnthropic path)
export LLM_PROVIDER=anthropic
export LLM_BASE_URL=https://api.z.ai/api/anthropic
export LLM_MODEL_NAME=glm-5.1
export OPENAI_API_KEY=$GLM_API_KEY

# Fraud triage demo mode
export ENVIRONMENT=demo

# Insights agent key alias
export ZHIPUAI_API_KEY=$GLM_API_KEY
```

## SEO Keywords

enterprise ai agents, langgraph agents, fraud triage ai, customer support ai automation, llm evaluation platform, fastapi multi-agent api, ad insights agent
