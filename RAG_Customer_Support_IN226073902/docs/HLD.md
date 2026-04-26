# High-Level Design (HLD)

## 1. System Overview

### Problem Definition
Customer support systems often rely on large documents like FAQs, manuals, and policies. Traditional approaches have limitations:

- Rule-based bots → limited coverage  
- LLM-only bots → hallucination risk  

We need a system that provides **accurate, context-aware answers grounded in real documents**, while also handling uncertain queries safely.

---

### Solution
This project implements a **RAG-based Customer Support Assistant** that:

- Processes a PDF knowledge base  
- Retrieves relevant information using embeddings  
- Generates answers using an LLM (Groq)  
- Uses LangGraph for workflow control  
- Supports Human-in-the-Loop (HITL) escalation  

---

### Scope of the System

**In Scope:**
- PDF ingestion (single knowledge base)
- Chunking + embedding + storage in ChromaDB
- Query-based retrieval
- LangGraph workflow (Input → Process → Output)
- Conditional routing (auto answer / escalate)
- CLI-based interaction

**Out of Scope:**
- Authentication and user roles
- Full web application UI
- Multi-document large-scale system
- Long-term conversation memory

---

## 2. Architecture Diagram
```text
User Query (CLI)
      ↓
LangGraph Workflow
(Input → Process → Output)
      ↓
Retrieval Layer (ChromaDB)
      ↓
Relevant Context
      ↓
LLM (Groq)
      ↓
Routing Decision
   ↙        ↘
Answer     HITL (Human)
   ↓          ↓
 Final Response
```

---

## 3. Component Description

### Document Loader

- Loads PDF using `PyPDFLoader`  
- Extracts text into structured documents  

---

### Chunking Strategy

- Uses recursive text splitter  
- Chunk size: ~500–1000 characters  
- Overlap used to maintain context continuity  

---

### Embedding Model

- Uses HuggingFace embeddings  
- Converts text into vector representations  

---

### Vector Store (ChromaDB)

- Stores embeddings locally  
- Enables fast similarity-based retrieval  

---

### Retriever

- Fetches top relevant chunks based on similarity  
- Used during query processing  

---

### LLM (Groq)

- Generates final answer using retrieved context  
- Ensures grounded responses (no hallucination)  

---

### Graph Workflow Engine (LangGraph)

- Controls system flow using nodes  
- Implements:
  - Process Node  
  - Output Node  
- Supports conditional routing  

---

### Routing Layer

- Decides whether:
  - Answer automatically  
  - Escalate to human  

- Based on:
  - Context availability  
  - Answer confidence  

---

### HITL Module (Human-in-the-Loop)

- Handles complex or unknown queries  
- Allows manual response input  

---

## 4. Data Flow

### Ingestion Flow

1. Load PDF  
2. Extract text  
3. Split into chunks  
4. Generate embeddings  
5. Store in ChromaDB  

---

### Query Flow

1. User enters query  
2. Query sent to workflow  
3. Retriever finds relevant chunks  
4. Context passed to LLM  
5. LLM generates answer  
6. Routing decision:
   - If confident → return answer  
   - Else → escalate to HITL  

---

## 5. Technology Choices

### ChromaDB

- Lightweight and easy to use  
- Suitable for local development  

---

### LangGraph

- Enables structured workflow control  
- Supports state-based decision making  

---

### Groq LLM

- Fast inference speed  
- Suitable for real-time response generation  

---

### HuggingFace Embeddings

- Open-source and efficient  
- Good semantic understanding  

---

## 6. Scalability Considerations

### Handling Large Documents

- Use chunking strategy  
- Optimize chunk size and overlap  

---

### Increasing Query Load

- Introduce caching for repeated queries  
- Deploy as API service (future scope)  

---

### Latency Optimization

- Use fast LLM models (Groq)  
- Limit retrieved context size  

---

## 7. Safety and Reliability

- System avoids hallucination using RAG  
- Escalates uncertain queries to human  
- Ensures reliable customer support responses  

---

## Conclusion

This system combines:

- Retrieval (accuracy)  
- Generation (flexibility)  
- Workflow control (decision-making)  
- Human fallback (reliability)  

It provides a scalable and trustworthy solution for customer support automation.