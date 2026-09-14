# Software Requirements Specification (SRS) — AgenticFlow AI

**Project Name:** AgenticFlow AI  
**Author:** Nachiket Gadilohar  

---

## 1. Functional Requirements
- **FR-GRAPH-01**: System MUST execute StateGraph nodes asynchronously using Python asyncio.
- **FR-CHK-01**: System MUST save state checkpoints to Redis after each node execution.
- **FR-HUMAN-01**: System MUST support resuming interrupted graphs via API call /api/graph/resume.
