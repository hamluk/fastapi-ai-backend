# fastapi-ai-backend

## 📦 Project Scope & Article Series Context

This repository, **fastapi-ai-backend**, serves as a reference implementation for designing backend-first AI systems using FastAPI.

Rather than focusing on UI demos or prompt-only experiments, the repository demonstrates how AI components can be treated as first-class backend services: explicitly wired, validated, testable, and evolvable.

Throughout the repository and the accompanying articles, a concrete example called the **InsightAgent** is used as a guiding implementation. The InsightAgent evolves step by step across multiple branches, showcasing how a simple LLM-powered endpoint can grow into a structured, production-oriented AI agent backend.


---

## 📂 Series Overview

| Part | Title                                | Blog Post                                                                                                   | Code                                                                    |
| ---- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1️⃣   | **Building Production-Ready AI Backends with FastAPI** | [Read on dev.to](https://dev.to/hamluk/building-production-ready-ai-backends-with-fastapi-4352) | - |
| 2️⃣   | **From LangChain Demos to a Production-Ready FastAPI Backend** | [Read on dev.to](https://dev.to/hamluk/from-langchain-demos-to-a-production-ready-fastapi-backend-1c0a) | [Branch: part-2](https://github.com/hamluk/fastapi-ai-backend/tree/part-2) |
| 3️⃣   | **Building Production-Ready RAG in FastAPI with Vector Databases** | [Read on dev.to](https://dev.to/hamluk/building-production-ready-rag-in-fastapi-with-vector-databases-39gf) | [Branch: part-3](https://github.com/hamluk/fastapi-ai-backend/tree/part-3) |
| 4️⃣   | **Introducing AI Agents as Backend Services** | _coming soon_ | [Branch: part-4](https://github.com/hamluk/fastapi-ai-backend/tree/part-4) |

---

## 🧭 Branches & Learning Path

This repository is structured as a progressive learning path that mirrors the accompanying article series on dev.to  
[Read the articles here.](https://dev.to/hamluk/building-production-ready-ai-backends-with-fastapi-4352)

Each branch represents a specific stage in the evolution of the backend architecture, while continuing to build on the same core example leading to the **InsightAgent**.

- **part-2**  
  Introduces a basic FastAPI endpoint with LangChain integration and structured responses.

- **part-3**  
  Adds Retrieval Augmented Generation (RAG), vector database integration, and dependency-injected retrievers.

- **part-4**  
  Introduces the InsightAgent as a dedicated backend service with similarity thresholds, explicit agent boundaries, and validated insight extraction.
Backend-first AI agent for extracting actionable insights from structured knowledge bases

---

## 🚀 InsightAgent

The **InsightAgent** is a backend-oriented AI agent that answers questions by extracting insights from a curated knowledge base. Instead of exposing an LLM directly, the agent operates behind a FastAPI endpoint, integrates Retrieval Augmented Generation via dependency injection, and produces structured, validated responses that can be consumed by other systems.


---

## 🧩 What the InsightAgent Does

* Accepts a question via a FastAPI endpoint 
* Retrieves relevant knowledge from a vector database using RAG 
* Applies similarity thresholds to ensure relevance 
* Uses an AI agent to extract and formulate insights 
* Returns structured, validated output via Pydantic models 
* If no relevant knowledge exists, the agent responds gracefully instead of hallucinating.

---

## 🏗 Architecture Overview

High-level flow

FastAPI Endpoint  
→ Dependency Injection (Settings, LLM, Vector Store, Retriever, Agent)  
→ Retriever (Similarity Threshold Applied)  
→ Insight Agent  
→ Structured Insight (Pydantic)  
→ API Response  

Core principles

* Explicit contracts
* Explicit dependencies
* No hidden state
* No prompt-only control flow

---

## ✨ Key Features

- Backend-first AI architecture: AI logic is treated like any other backend component, not as a special case  
- Retrieval Augmented Generation with control: Similarity scores are explicitly evaluated and filtered before the agent runs  
- Deterministic and structured outputs: All responses conform to strict Pydantic models for reliability and integration safety  
- Dependency Injection for AI components: LLMs, vector stores, retrievers, and agents are injected via FastAPI `Depends`  
- Clean separation of concerns: Endpoints orchestrate, retrievers retrieve, agents reason, models validate  
- Forward-compatible design: The architecture supports adding tools, workflows, state handling, and error strategies without refactoring endpoints  

---

## 🏁 Quick Start

### Requirements

* Python 3.13+
* Poetry
* OpenAI API key
* Running Qdrant instance (local or remote)

### 🔧 Installation
```bash
poetry install
```

### 🔐 Environment Variables

Create a .env file in the project root from the .env_example file.

### 📘 How to Use

1. Upload document chunks to the vector store via the /upload/chunks endpoint
2. Query insights via the /insight/query endpoint
3. Receive structured insights with confidence and metadata
4. Extend with agents, tools, or workflows as needed

This setup is ideal for demos, experiments, and architectural learning without UI overhead.

---

## 🔒 Privacy & Cost Notice

* All LLM calls use your personal OpenAI API key
* API usage incurs costs depending on model and volume
* Do not upload sensitive or confidential data
* This project is a reference architecture, not a drop-in production solution

---

## 👤 Author

Lukas Hamm

🔗[https://www.lukashamm.dev](https://www.lukashamm.dev)  
📧 [lukas@lukashamm.dev](lukas@lukashamm.dev)  
💼 [https://www.linkedin.com/in/lukashamm-dev](https://www.linkedin.com/in/lukashamm-dev)

---

## 🏷 GitHub Topics

`ai-agent` · `fastapi` · `langchain` · `rag` · `backend-architecture` · `pydantic` · `vector-database` · `qdrant` · `dependency-injection` · `llm` · `ai-backend`
