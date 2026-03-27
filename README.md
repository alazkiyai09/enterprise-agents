# enterprise-agents

Unified LangGraph agent repo created from `enterprise-ai-systems` for support, fraud triage, ad insights, and LLM evaluation.

## Included sources

- `src/support_app` from `CustomerSupport-Agent`
- `src/fraud_triage` from `FraudTriage-Agent`
- `src/ad_insights` from `AdInsights-Agent`
- `src/llmops_eval` and `src/dashboard` from `LLMOps-Eval`
- Stable wrappers under `src/agents`, `src/evaluation`, `src/memory`, and `src/monitoring`

## Unified API shell

Run:

```bash
uvicorn src.api.main:app --reload
```

Key routes:

- `POST /api/v1/agents/support/chat`
- `POST /api/v1/agents/fraud/alerts`
- `POST /api/v1/agents/insights/analyze`
- `POST /api/v1/eval/run`
- `GET /health`

