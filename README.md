# ⚡ AgenticFlow AI: Enterprise Multi-Agent Systems & LangGraph Production Suite

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2%2B-orange.svg?style=for-the-badge&logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-green.svg?style=for-the-badge&logo=langchain&logoColor=white)](https://github.com/langchain-ai/langchain)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991.svg?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude--3.5-D97706.svg?style=for-the-badge&logo=anthropic&logoColor=white)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-Apache--2.0-lightgrey.svg?style=for-the-badge)](https://github.com/nachiket0987/agenticflow-ai)

> **AgenticFlow AI** is a production-grade, state-of-the-art framework and architectural blueprint for designing, orchestrating, evaluating, and deploying stateful **Multi-Agent Systems** using LangGraph, LangChain, Python, OpenAI GPT-4o, Anthropic Claude, and Tavily AI.

---

## 📋 Executive Overview

As Generative AI matures, enterprise applications require moving beyond monolithic, single-prompt models toward **stateful, graph-based multi-agent architectures**. **AgenticFlow AI** solves the core challenges of determinism, latency control, memory management, tool discovery, and real-time governance in multi-agent workflows.

Whether you are building autonomous research pipelines, real-time supply chain managers, or automated paper screening agents, **AgenticFlow AI** provides the foundational primitives, design patterns, and deployment configurations required for enterprise reliability.

---

## 🔑 Key Features & Core Capabilities

### 1. 🤖 Advanced Agent Execution Paradigms
- **ReAct (Reasoning + Acting)**: Interleaved reasoning, dynamic tool execution, and observation feedback loops.
- **PAL (Program-Aided Language Models)**: Offloads math, statistical calculations, and precise operations to an isolated Python sandbox (`exec()`), eliminating LLM arithmetic hallucinations.
- **Plan-and-Execute**: Strategic task decomposition phase followed by deterministic step-by-step tool execution and final consensus synthesis.
- **Supervisor Multi-Agent Routing**: Central orchestrator routing tasks across specialized domain agents (Math, Research, Technical Writing, System Analytics).
- **Reflection & Self-Correction**: Autonomous generate $\rightarrow$ critique $\rightarrow$ revise cycles for continuous output refinement without tool dependencies.

### 2. 🏬 Enterprise Industrial Solutions
- **`agentic_screener`**: Systematic academic literature screening & summarization pipeline with PDF parsing, inclusion/exclusion filtering, reflection evaluation, and CSV synthesis.
- **`warehouse_architectures`**: Multi-agent graph managing inventory replenishment, fleet logistics, order fulfillment, and decentralized node routing.
- **`warehouse_monitors`**: Real-time governance suite covering operational safety, ethical boundaries, anomaly detection, and belief-state tracking.

### 3. 🧩 Production Solution Design Patterns
- **Asynchronous Messaging**: Queue-based decoupling for non-blocking agent communication.
- **Batch Processing**: Parallelized workload distribution with stateful batch queues.
- **Coherent Memory Architectures**: Short-term, long-term, and episodic memory management across multi-turn graph states.
- **Event Hub Internals**: Event-driven pub/sub architecture for real-time agent reactive triggers.
- **Dynamic Tool Discovery**: Registry-backed tool indexing enabling agents to discover and invoke tools on demand.
- **Financial Fraud Detection**: Batch processing pipeline for real-time risk assessment and regulatory compliance reporting.

---

## 📐 System Architecture

### 1. Supervisor Multi-Agent Orchestration Flow

```mermaid
graph TD
    User([User Request / API Payload]) --> Supervisor[Supervisor Orchestrator Agent]
    
    Supervisor -->|Task: Calculations & Math| MathAgent[Math Specialist Agent]
    Supervisor -->|Task: Literature Search| ResearchAgent[Research & Literature Agent]
    Supervisor -->|Task: Document Synthesis| WriterAgent[Technical Writer Agent]
    
    MathAgent --> Sandbox[Python Code Execution Sandbox]
    ResearchAgent --> SearchTool[Tavily Academic & Web Search]
    WriterAgent --> Formatter[Markdown & Report Formatter]
    
    Sandbox -->|Execution Result| State[Stateful Graph Context]
    SearchTool -->|Search Results| State
    Formatter -->|Formatted Output| State
    
    State --> Supervisor
    Supervisor -->|Final Consensus Reached| FinalOutput([Final Consolidated Output])
```

### 2. Core Execution Loop (State Graph Engine)

```mermaid
graph LR
    START([START]) --> AgentNode[Agent Decision Node]
    AgentNode -->|tool_calls Present| ToolNode[Tool Execution Node]
    ToolNode -->|Return ToolMessage| AgentNode
    AgentNode -->|No tool_calls / Complete| END([END])
```

---

## 📈 Empirical Benchmarks & Pattern Comparison

The repository includes a dedicated benchmarking suite ([`langgraph_examples/pal_react_plan_execute`](langgraph_examples/pal_react_plan_execute)) comparing the three major agent execution paradigms under controlled, identical workload conditions:

| Evaluation Metric | **PAL (Program-Aided)** | **ReAct (Reason + Act)** | **Plan-and-Execute** |
| :--- | :--- | :--- | :--- |
| **LLM Call Overhead** | **2–3 calls** (Lowest cost & latency) | Dynamic ($N$ loop iterations) | $2 + N$ calls (Plan + execution + finalizer) |
| **Math & Logic Accuracy** | **100% Deterministic** (Python interpreter) | Error-prone on multi-step math | Depends on tool precision |
| **Tool Flexibility** | Fixed (Code sandbox only) | **High** (Dynamic, any tool in any order) | **Structured** (Fixed tools, planned sequence) |
| **Task Horizon / View** | Full program written upfront | Greedy (1 step at a time) | **Full explicit plan before execution** |
| **Failure Recovery** | Low (Single-shot code generation) | **High** (Dynamic retries on tool errors) | Medium (Requires replanner node) |
| **Debuggability & Audit** | **Easy** (Inspect generated Python code) | Hard (Emergent runtime call graph) | **Easy** (Inspectable plan upfront) |
| **Primary Failure Mode** | Python code syntax/logic error | Infinite loop / tool selection error | Flawed initial plan |

---

## ⚡ Developer Quickstart & Installation

### 1. Prerequisites
- **Python 3.10+**
- **Git**
- **Virtual Environment Tool (`venv` or `conda`)**

### 2. Clone Repository & Setup Environment

```bash
# Clone the repository
git clone https://github.com/nachiket0987/agenticflow-ai.git
cd agenticflow-ai

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 3. Install Package in Editable Mode

```bash
# Install core dependencies and package CLI
pip install -e .
```

### 4. Configure Credentials (`.env`)

Copy the environment template and insert your API keys:

```bash
cp .env.example .env
```

Edit `.env`:
```env
OPENAI_API_KEY=sk-proj-your-openai-api-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key
TAVILY_API_KEY=tvly-your-tavily-api-key
```

---

## 🚀 Execution & Usage Examples

### ReAct Agent with Tools
```bash
python langgraph_examples/example3_agent_with_tools.py
```

### Supervisor Multi-Agent System
```bash
python langgraph_examples/example4_multi_agent_supervisor.py
```

### Automated Paper Screener & Summarizer
```bash
python langgraph_examples/example12_paper_screener.py
```

### Industrial Warehouse Operations
```bash
python warehouse_architectures/main.py
```

### Benchmark Suite Comparison
```bash
# PAL Pattern
python langgraph_examples/pal_react_plan_execute/example_pal.py

# ReAct Pattern
python langgraph_examples/pal_react_plan_execute/example_react.py

# Plan-and-Execute Pattern
python langgraph_examples/pal_react_plan_execute/example_plan_execute.py
```

---

## 🗂️ Comprehensive Directory Structure

```
agenticflow-ai/
│
├── Agentic AI Solution Design Patterns/  # Enterprise design patterns
│   ├── async_messaging/                  # Async queue decoupling
│   ├── batch_processing/                 # Stateful batch queues
│   ├── chain_of_thought/                 # Reasoning trace comparative evaluation
│   ├── coherent_memory/                  # Multi-tier agent memory management
│   ├── event_driven/                     # Event hub pub/sub platform
│   ├── expert_team/                      # Specialized agent collaboration
│   ├── financial_fraud_batch/            # Risk assessment & compliance reporting
│   ├── logistics_async/                  # Fleet logistics orchestration
│   └── tool_discovery/                   # Dynamic tool registry & search
│
├── agentic_screener/                     # Systematic literature review engine
│   ├── agents/                           # Criterion inclusion/exclusion screeners
│   ├── config.py                         # Screening thresholds & model selection
│   └── run.py                            # End-to-end execution pipeline
│
├── data/                                 # Sample order databases, pricing tables, & PDFs
├── docs/                                 # Technical architecture specifications & guides
├── examples/                             # Architectural perception, reasoning, & action modules
├── langchain_examples/                   # LangChain prerequisite tutorials
│
├── langgraph_examples/                   # Progressive LangGraph implementation suite
│   ├── example1_hello_world.py           # Pure state graph (No LLM)
│   ├── example2_chatbot.py               # Stateful LLM chatbot with MessagesState
│   ├── example3_agent_with_tools.py      # ReAct agent with ToolNode & tools_condition
│   ├── example4_multi_agent_supervisor.py# Multi-agent routing with structured output
│   ├── example5_research_pipeline.py     # Research assistant pipeline
│   ├── example10_reflection_agent.py     # Reflection loop (Generate -> Review -> Revise)
│   ├── example11_multi_agent_router.py   # Specialized domain routing
│   ├── example12_paper_screener.py       # Literature screening pipeline
│   ├── example13_paper_summarizer.py     # PDF download & structured summary
│   ├── example14_paper_report.py         # Academic synthesis report generator
│   └── pal_react_plan_execute/           # Benchmark suite (PAL vs ReAct vs Plan-Execute)
│
├── warehouse_architectures/              # Multi-agent supply chain & inventory management
├── warehouse_monitors/                   # Real-time safety, ethics, & anomaly monitors
├── .env.example                          # Environment variable configuration template
├── pyproject.toml                        # Modern PEP 621 package build configuration
├── requirements.txt                      # Project dependency specification
└── setup.py                              # Standard Python package setup
```

---

## 🛡️ Production Deployment & Tracing

### 1. LangSmith Observability & Tracing
Enable real-time tracing of node execution latencies, token consumption, and state transitions by adding the following to `.env`:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=lsv2_pt_your_key_here
LANGCHAIN_PROJECT=agenticflow-ai
```

### 2. Containerized Deployment (Docker)
Build and run `AgenticFlow AI` in an isolated Linux container:

```bash
docker build -t agenticflow-ai:latest .
docker run -d --env-file .env -p 8000:8000 agenticflow-ai:latest
```

### 3. REST API & Cloud Orchestration
Compile state graphs directly into microservices using LangGraph CLI / FastAPI:

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
- 💼 **LinkedIn**: [linkedin.com/in/nachiket-gadilohar-profile/](https://linkedin.com/in/nachiket-gadilohar-profile/)

---

## 📄 License

This repository is maintained for open developer and enterprise educational usage under the **Apache 2.0 License**.
