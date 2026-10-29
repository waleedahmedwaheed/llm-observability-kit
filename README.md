# LLM Observability Kit

Lightweight LLM eval and tracing kit for prompts, latency, cost, and quality checks.

Ship AI features with confidence: measure what runs, catch regressions, and compare prompt versions.

## Capabilities

- Request tracing (prompt, model, tokens, latency)
- Golden-set offline evaluations
- Simple scoring hooks (exact match, contains, LLM-as-judge stub)
- Export-friendly JSON logs for dashboards

## Project layout

```text
src/
  tracer.py      # wrap LLM calls with metrics
  evals.py       # run offline evaluation suites
  scorers.py     # quality scoring helpers
  reporters.py   # print / write summaries
examples/
  sample_suite.json
requirements.txt
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

python -m src.evals --suite examples/sample_suite.json
```

## What to track

| Signal | Why it matters |
| --- | --- |
| Latency | UX and SLA |
| Tokens / cost | Budget control |
| Failure rate | Reliability |
| Eval score | Quality over time |

## Suggested workflow

1. Wrap production/dev LLM calls with the tracer  
2. Keep a small golden suite for critical prompts  
3. Fail CI when quality or cost thresholds regress  

## License

MIT
