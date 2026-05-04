---
file_id: CONCEPT_Wiki_vs_RAG
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
confidence: 0.7
sources: ["3-resources/raw/sources/AIMET_Karpathys_LLM_Wiki_Guide.md"]
---

# CONCEPT: Wiki vs RAG (DRAFT)

## Core Principle (Raw Snippets)
- RAG Problem: “The LLM is rediscovering knowledge from scratch on every question. There's no accumulation.”
- Wiki Solution: “Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki.”
- Compounding Effect: “The wiki is a persistent, compounding artifact.”
- Processing time: RAG is at query time (ephemeral); Wiki is at ingest time (durable).

## Comparison Matrix
- RAG: starts fresh each query, may miss contradictions.
- Wiki: pre-built, cross-referenced, flags contradictions during ingestion.

## 4F Reflection (Pending Human Review)
- Facts: RAG is the dominant pattern today (NotebookLM, ChatGPT). Karpathy argues it's inefficient for long-term knowledge.
- Feelings: [Waiting for User]
- Findings: [Waiting for User]
- Futures: [Waiting for User]
