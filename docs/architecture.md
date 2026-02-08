# Application Map — Agentic Food Procurement Assistant

**Domain:** Food procurement (healthcare & senior living)  
**Frontend:** React + Next.js  
**Backend:** Python (FastAPI)  
**AI:** Python + LangChain  
**Data Sources:** Mock Contracts API + Mock Inventory API  
**External APIs:** None 

---
## High-Level Flow
    User
    ↓
    Frontend (React / Next.js Chat UI)
    ↓
    Backend API (Python / FastAPI)
    ↓
    AI Orchestration Layer (LangChain Agent)
    ↓
    [Tool Calls]
    ├─ Mock Contracts API
    └─ Mock Inventory API
    ↓
    Agent Reasoning & Decision Support
    ↓
    Structured Recommendation / Order Draft
    ↓
    Frontend Rendered Response

### Core Principle
- **The frontend presents**
- **The backend orchestrates**
- **The AI reasons**
This separation mirrors how real enterprise procurement systems are designed.

---
## Industry-Standard Architecture (By Service)
### Frontend — React Web App (Next.js)
**Responsibilities**
- Collect user input (procurement questions, order issues)
- Display chat responses and recommendations
- Render compliance flags and order drafts
- Handle loading and error states
- Remain stateless with respect to business logic
**Key principle**
- The frontend never talks directly to data sources or the LLM  
- All intelligence flows through the backend API
**Suggested structure**
    frontend/
    ├── app/
    │ ├── page.tsx # Main chat page
    │ └── layout.tsx
    ├── components/
    │ ├── ChatWindow.tsx
    │ ├── MessageBubble.tsx
    │ └── OrderDraft.tsx
    ├── services/
    │ └── apiClient.ts # Calls backend /chat endpoint
    └── README.md

---
### Backend — API & Orchestration (Python / FastAPI)
**Responsibilities**
- Accept chat requests from the frontend
- Validate and normalize input
- Invoke the AI agent
- Enforce request boundaries (timeouts, error handling)
- Return structured, predictable responses
**What the backend does NOT do**
- No reasoning
- No product selection
- No substitution logic
**Suggested structure**
    backend/
    ├── app/
    │ ├── main.py # FastAPI entrypoint
    │ ├── api/
    │ │ └── chat.py # POST /chat
    │ ├── services/
    │ │ └── agent.py # Calls AI layer
    │ ├── schemas/
    │ │ ├── request.py
    │ │ └── response.py
    │ └── config.py
    └── README.md

---
### AI Service — Agentic Reasoning Layer (Python / LangChain)
**Responsibilities**
- Interpret procurement-related user intent
- Identify the workflow type:
  - Stock-out resolution
  - Contract compliance validation
  - Curated product search
- Select and call the appropriate tools
- Reason across constraints
- Generate explainable recommendations

**Minimal, defensible agent loop**
1. Receive user goal
2. Classify procurement intent
3. Decide which tools are needed
4. Call tools and gather structured data
5. Reason across constraints
6. Respond with recommendation + explanation

**Suggested structure**
    ai/
    ├── agent/
    │ ├── procurement_agent.py
    │ ├── prompts.py
    │ └── decision_logic.py
    ├── tools/
    │ ├── contracts_tool.py
    │ └── inventory_tool.py
    ├── schemas/
    │ ├── product.py
    │ ├── contract.py
    │ └── inventory.py
    ├── data_access/
    │ └── loaders.py # Loads mock JSON data
    └── README.md

---
## Tooling Layer
### Mock Contracts API (Source of Truth)
Provides:
- Approved brands
- Pack sizes and units
- Supplier constraints
- Dietary and formulary requirements
- Contract effective dates
Used to:
- Validate product compliance
- Enforce ordering rules
- Reject non-compliant recommendations

---
### Mock Inventory API (Source of Truth)
Provides:
- Product availability
- Hard stock-outs (0 available)
- Partial stock-outs (limited quantity)
- Quantity constraints
Used to:
- Detect fulfillment issues
- Trigger substitution workflows
- Support order revision and re-fulfillment

---
## Design Guarantees
- The LLM does **not** invent products
- All recommendations are grounded in structured mock data
- Decisions are explainable and traceable
- The system produces recommendations, not automated actions
- Humans remain in the loop

---
## Summary
    The application is a procurement decision-support chatbot where a Python backend orchestrates requests, a LangChain agent reasons across inventory and contract constraints, and a Next.js frontend presents structured, explainable recommendations to users.
