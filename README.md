# AI Market Intelligence Platform

An AI-powered market research and competitor intelligence platform built using deterministic AI workflows, structured outputs, and production-inspired engineering practices.

The system analyzes a target market, discovers competitors, performs strategic analysis, validates findings, and generates executive reports while demonstrating real-world AI platform concepts such as observability, guardrails, tracing, and evaluations.

---

## Overview

Traditional multi-agent systems often rely on autonomous agent conversations, making them difficult to debug, govern, and reproduce.

This project intentionally adopts a deterministic workflow architecture where specialized nodes execute a bounded responsibility and exchange structured data contracts instead of free-form text.

The objective is to demonstrate production-grade AI engineering patterns rather than agent chaining.

---

## Features

* Competitor discovery and market research
* SWOT analysis generation
* Strategic product recommendations
* Executive report generation
* Structured outputs with Pydantic
* Fact-checking and confidence scoring
* Guardrails and PII detection
* Request tracing and observability
* Evaluation framework for quality measurement
* Redis-backed caching and rate limiting

---

## Architecture

```text
Streamlit UI
       ↓
FastAPI Backend
       ↓
Request Middleware
       ↓
PII Detection
Input Validation
Rate Limiting
       ↓
LangGraph Workflow
       ↓
Research Node
       ↓
Analysis Node
       ↓
Fact Check Node
       ↓
Critic Node
       ↓
Writer Node
       ↓
Output Validation
       ↓
Persistence Layer
       ↓
Langfuse Observability
```

---

## Workflow

```text
START
↓
Validate Request
↓
Research
↓
Analysis
↓
Fact Check
↓
Critic
↓
Generate Report
↓
Persist Results
↓
END
```

---

## Tech Stack

| Layer            | Technology       |
| ---------------- | ---------------- |
| Frontend         | Streamlit        |
| API              | FastAPI          |
| Workflow Engine  | LangGraph        |
| LLM              | Gemini 2.5 Flash |
| Search           | Tavily           |
| Observability    | Langfuse         |
| Cache            | Redis            |
| Storage          | SQLite           |
| Guardrails       | LLM Guard        |
| PII Detection    | Presidio         |
| Evals            | DeepEval         |
| Containerization | Docker           |

---

## Project Structure

```text
market-intelligence-platform/

app/

├── api/
├── workflows/
├── nodes/
├── services/
├── schemas/
├── guardrails/
├── evals/
├── ui/
├── config/
└── README.md
```

---

## Engineering Principles

### Deterministic Workflows

Each node has a single responsibility and exchanges structured contracts instead of free-form text.

### Observability First

Every workflow execution is traced with latency, token usage, retries, and cost metrics.

### Safety by Design

Requests are validated using PII masking, prompt injection detection, and output validation before results are returned.

### Evaluation Driven Development

Benchmark datasets and automated evaluations measure hallucination rate, citation accuracy, and response quality.

### Evolutionary Architecture

Execution is intentionally abstracted to support future migration from an in-process executor to RabbitMQ or Temporal without changing workflow logic.

---

## Future Improvements

* Browser-based research enrichment
* Human-in-the-loop approvals
* Multi-market comparative analysis
* Historical trend analysis
* Vector search over previous reports
* Distributed worker execution

---

## Why this project?
This project was built to explore production AI platform engineering concepts beyond simple agent chaining.

The focus is on designing reliable, observable, and maintainable AI systems that can evolve from a single-node deployment into a distributed architecture while preserving deterministic behavior and reproducibility.
