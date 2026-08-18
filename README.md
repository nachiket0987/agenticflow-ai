# 🤖 AgenticFlow AI: Enterprise Multi-Agent Workflows & LangGraph Suite

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2%2B-orange.svg)](https://github.com/langchain-ai/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-green.svg)](https://github.com/langchain-ai/langchain)
[![Architecture](https://img.shields.io/badge/Architecture-Stateful%20Multi--Agent-purple.svg)](#system-architecture--core-paradigms)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/nachiket0987/agenticflow-ai)

> **AgenticFlow AI** is a state-of-the-art enterprise framework and architectural reference suite for building, orchestrating, monitoring, and scaling stateful **Multi-Agent Systems** using LangGraph, LangChain, OpenAI, and Anthropic Claude.

---

## 📌 Executive Summary & Key Features

Modern AI engineering is shifting from single-prompt generation to **autonomous multi-agent graphs**. **AgenticFlow AI** provides a complete end-to-end blueprint—from mathematical foundations to real-world industrial deployments—enabling reliable, self-correcting, and highly scalable AI agent systems.

### 🔥 Core Features & Capabilities

- 🧠 **Advanced Agent Patterns**:
  - **ReAct (Reasoning + Acting)**: Interleaved thinking, tool execution, and dynamic observation loops.
  - **PAL (Program-Aided Language Models)**: Offloads math and precise logical steps directly to an executable Python sandbox (`exec()`).
  - **Plan-and-Execute**: High-level planner decomposes complex objectives before task-bound executors process steps sequentially.
  - **Reflection & Self-Correction**: Autonomous generate $\rightarrow$ review $\rightarrow$ critique $\rightarrow$ revise loops without external tool reliance.
- 🏢 **Production Industrial Systems**:
  - **Systematic Paper Screener & Summarizer (`agentic_screener`)**: Automated PDF extraction, structured synthesis, evaluation, and CSV export.
  - **Warehouse Automation Systems (`warehouse_architectures`)**: Stateful multi-agent graphs for inventory control, order fulfillment, routing, and replenishment.
  - **Real-Time Governance & Monitors (`warehouse_monitors`)**: Anomaly detection, compliance auditing, safety monitoring, and ethical guardrails.
- 🛠️ **Enterprise Design Patterns**:
  - Asynchronous message queues, batch processing pipelines, coherent memory architectures, event-driven message hubs, tool registries, and financial fraud batch monitors.

---

## 🏗️ System Architecture & Core Paradigms

### 1. Supervisor-Managed Multi-Agent Routing

```
                        ┌────────────────────────┐
                        │     User Input / API   │
                        └───────────┬────────────┘
                                    │
                                    ▼
                        ┌────────────────────────┐
                        │   Supervisor Router    │
                        └─────┬──────┬──────┬────┘
                              │      │      │
            ┌─────────────────┘      │      └──────────────────┐
            ▼                        ▼                         ▼
  ┌──────────────────┐     ┌──────────────────┐      ┌──────────────────┐
  │   Math Specialist │     │ Research Agent   │      │ Technical Writer │
  └─────────┬────────┘     └────────┬─────────┘      └────────┬─────────┘
            │                        │                         │
            ▼                        ▼                         ▼
  ┌──────────────────┐     ┌──────────────────┐      ┌──────────────────┐
  │  Python Sandbox  │     │ Literature Search│      │  Draft Formatter │
  └─────────┬────────┘     └────────┬─────────┘      └────────┬─────────┘
            │                        │                         │
            └──────────────────┐     │     ┌───────────────────┘
                               ▼     ▼     ▼
                        ┌────────────────────────┐
                        │  Stateful Consolidation│
                        └───────────┬────────────┘
                                    │
                                    ▼
                        ┌────────────────────────┐
                        │     Final Output       │
                        └────────────────────────┘
```

---

## 📊 Benchmark Comparison & Empirical Results

The repository includes a comprehensive benchmark suite ([`langgraph_examples/pal_react_plan_execute`](langgraph_examples/pal_react_plan_execute)) comparing the three major agent execution paradigms under identical workload conditions:

| Dimension | **PAL (Program-Aided)** | **ReAct (Reason + Act)** | **Plan-and-Execute** |
| :--- | :--- | :--- | :--- |
| **LLM Call Overhead** | **2–3 calls** (Lowest cost & latency) | Dynamic ($N$ loop iterations) | $2 + N$ calls (Plan + execution + finalizer) |
| **Math & Logic Accuracy** | **100% Deterministic** (Python interpreter) | Error-prone on multi-step math | Depends on tool precision |
| **Tool Usage** | Single tool (Python Code Sandbox) | **Dynamic** (Any tool in any order) | **Structured** (Fixed tools, planned sequence) |
| **Task Horizon** | Full code written upfront | Greedy (1 step at a time) | **Full explicit plan before execution** |
| **Adaptability to Failure** | Low (Single-shot code generation) | **High** (Dynamic retries on tool errors) | Medium (Requires replanner node) |
| **Debuggability** | **Easy** (Inspect generated Python code) | Hard (Emergent runtime call graph) | **Easy** (Inspectable plan upfront) |
| **Primary Failure Mode** | Python code syntax/logic error | Infinite loop / tool selection error | Flawed initial plan |

---

## ⚡ Quickstart & Installation

### 1. Clone & Prerequisites

Ensure you have **Python 3.10+** installed on your system.

```bash
git clone https://github.com/nachiket0987/agenticflow-ai.git
cd agenticflow-ai
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 3. Install Package & Dependencies

```bash
# Install in editable mode
pip install -e .
```

### 4. Configure Environment Variables

Copy the `.env.example` template to `.env` and insert your credentials:

```bash
cp .env.example .env
```

Set your keys inside `.env`:
```env
OPENAI_API_KEY=sk-proj-your-openai-api-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key
TAVILY_API_KEY=tvly-your-tavily-api-key
```

---

## 🚀 Running Examples & Workflows

### ReAct Agent with Tools
```bash
python langgraph_examples/example3_agent_with_tools.py
```

### Supervisor Multi-Agent System
```bash
python langgraph_examples/example4_multi_agent_supervisor.py
```

### Paper Screener & Summarizer
```bash
python langgraph_examples/example12_paper_screener.py
```

### Warehouse Automation & Multi-Agent Operations
```bash
python warehouse_architectures/main.py
```

### Benchmark Strategy Comparison
```bash
python langgraph_examples/pal_react_plan_execute/example_pal.py
python langgraph_examples/pal_react_plan_execute/example_react.py
python langgraph_examples/pal_react_plan_execute/example_plan_execute.py
```

---

## 📁 Repository Structure

```
agenticflow-ai/
├── Agentic AI Solution Design Patterns/  # Enterprise design patterns (async, memory, event hub)
├── agentic_screener/                     # Automated paper screening & summarization pipeline
├── data/                                 # Sample datasets, paper PDFs, & mock store databases
├── docs/                                 # Technical documentation & design guides
├── examples/                             # Architectural perception & reasoning modules
├── langchain_examples/                   # LangChain prerequisite tutorials & primitives
├── langgraph_examples/                   # 14+ progressive LangGraph implementation guides
│   └── pal_react_plan_execute/           # Benchmark suite comparing PAL, ReAct, & Plan-Execute
├── warehouse_architectures/              # Multi-agent stateful supply chain & logistics system
├── warehouse_monitors/                   # Real-time compliance, ethics, & anomaly monitors
├── .env.example                          # Environment variable template
├── pyproject.toml                        # Modern PEP 621 build configuration
├── requirements.txt                      # Project dependencies
└── setup.py                              # Package installer
```

---

## 🌐 Production Deployment & Tracing

### LangSmith Observability
To trace agent graph states and node latencies in real time, enable LangSmith in `.env`:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_your_key_here
LANGCHAIN_PROJECT=agenticflow-ai
```

### Production API Deployment via FastAPI / LangGraph Cloud
You can package compiled `StateGraph` applications directly into REST API services using `langgraph-cli` or FastAPI endpoints:

```bash
langgraph build -t agenticflow-service
langgraph up
```

---

## 👨‍💻 Author & Contact

**Nachiket Gadilohar**  
*AI / ML Engineer & Agentic Systems Architect*

- 📧 **Email**: [nachiketlohar0306@gmail.com](mailto:nachiketlohar0306@gmail.com)
- 🐙 **GitHub**: [@nachiket0987](https://github.com/nachiket0987)
- 💼 **LinkedIn**: [Nachiket Gadilohar Profile](https://linkedin.com/in/nachiket-gadilohar-profile/)

---

## 📜 License

This project is maintained under the terms of open developer usage.
