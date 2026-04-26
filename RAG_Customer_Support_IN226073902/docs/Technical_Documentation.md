# Technical Documentation

---

## 1. Introduction

This document provides a detailed technical explanation of the **RAG-based Customer Support Assistant**.

The system uses:
- Retrieval-Augmented Generation (RAG)
- LangGraph workflow orchestration
- ChromaDB vector database
- Groq LLM for answer generation
- Human-in-the-Loop (HITL) for fallback

---

## 2. System Workflow Overview

The system follows this pipeline:

1. Load PDF document
2. Convert into chunks
3. Generate embeddings
4. Store in vector database
5. Accept user query
6. Retrieve relevant chunks
7. Generate answer using LLM
8. Apply routing logic
9. Return response or escalate

---

## 3. Module Breakdown

### 3.1 ingestion.py

**Purpose:** Load and process PDF

**Functions:**
- Load PDF using `PyPDFLoader`
- Split into chunks using text splitter

---

### 3.2 retrieval.py

**Purpose:** Create embeddings and vector store

**Functions:**
- Generate embeddings using HuggingFace
- Store vectors in ChromaDB
- Provide retriever object

---

### 3.3 rag_pipeline.py

**Purpose:** Generate final answer using LLM

**Process:**
- Retrieve context using retriever
- Build prompt
- Send request to Groq API
- Return generated response

---

### 3.4 routing.py

**Purpose:** Decide system behavior

**Logic:**
- If context exists → auto answer
- If no context → escalate

---

### 3.5 workflow.py

**Purpose:** Control system flow using LangGraph

**Nodes:**
- Process Node
- Output Node

---

### 3.6 hitl.py

**Purpose:** Handle escalation

**Functionality:**
- Takes human input
- Returns manual response

---

### 3.7 main.py

**Purpose:** Entry point

**Flow:**
- Load PDF
- Create vector DB
- Build workflow
- Accept user queries
- Return response

---

## 4. Data Processing

### 4.1 Chunking

- Method: RecursiveCharacterTextSplitter
- Chunk size: ~500–1000
- Overlap: ~100–150

---

### 4.2 Embeddings

- Model: HuggingFace (`all-MiniLM-L6-v2`)
- Converts text → vectors

---

### 4.3 Retrieval

- Uses similarity search
- Returns top-k relevant chunks

---

## 5. Prompt Design

The system uses structured prompts:
```text
You are a customer support assistant.

Answer ONLY from the given context.
If the answer is not available, reply:
"I don't know"

Context:
{context}

Question:
{query}
```

---

## 6. Routing Logic

### Auto Answer
- Context is available
- LLM produces valid answer

### Escalation
- No relevant context
- Uncertain response

---

## 7. Human-in-the-Loop (HITL)

### When triggered:
- No data found
- Query unclear
- LLM cannot answer

### Process:
1. System detects failure
2. Requests human input
3. Returns human response

---

## 8. API Flow (Internal)

### Input:
```json
{
  "query": "User question"
}
```

### Output
```json
{
  "answer": "Generated response",
  "route": "auto/escalate"
}
```
## 9. Error Handling
### Cases handled:
- Missing PDF → error message
- No chunks → fallback
- LLM failure → safe response
- API error → handled gracefully

## 10. Performance Considerations
- Fast inference using Groq
- Local vector DB (low latency)
- Efficient chunking

## 11. Limitations
- Single PDF support
- No UI (CLI only)
- No long-term memory

## 12. Future Improvements
- Web interface (React / Streamlit)
- Multi-document support
- Authentication system
- Chat history memory
- Better routing using confidence scoring

## 13. Conclusion

This system demonstrates a production-style RAG pipeline with:

- Accurate retrieval
- Controlled generation
- Workflow orchestration
- Human fallback

It ensures reliable and scalable customer support automation.