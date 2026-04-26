# Low-Level Design (LLD)

## 1. Introduction

The Low-Level Design (LLD) defines how the RAG-based Customer Support Assistant is implemented internally.  
It describes modules, data structures, workflow execution, and decision logic.

---

## 2. Module-Level Design

### 2.1 Document Processing Module
- Responsible for loading PDF documents
- Uses `PyPDFLoader`
- Outputs structured text documents

---

### 2.2 Chunking Module
- Splits large text into smaller chunks
- Uses Recursive Character Text Splitter
- Ensures overlapping chunks for better context retention

---

### 2.3 Embedding Module
- Converts text chunks into vector embeddings
- Uses HuggingFace embedding model
- Output: numerical vector representation

---

### 2.4 Vector Storage Module
- Stores embeddings in ChromaDB
- Supports similarity search
- Persistent local storage

---

### 2.5 Retrieval Module
- Retrieves top-k relevant chunks based on query
- Uses vector similarity search
- Output: relevant document chunks

---

### 2.6 Query Processing Module
- Accepts user query
- Sends query to retriever
- Prepares context for LLM

---

### 2.7 Graph Execution Module (LangGraph)
- Controls workflow execution
- Nodes:
  - Process Node
  - Output Node
- Manages state transitions

---

### 2.8 HITL Module
- Handles escalation cases
- Takes human input when needed
- Returns manual response

---

## 3. Data Structures

### 3.1 Document Representation
```python
{
  "page_content": "text data",
  "metadata": {}
}
```
### 3.2 Chunk Format
```python
{
  "chunk_id": int,
  "text": "chunk content"
}
```
### 3.3 Embedding Structure
```python
{
  "vector": [float, float, ...]
}
```
### 3.4 Query-Response Schema
```python
{
  "query": str,
  "context": str,
  "answer": str,
  "route": str
}
```
### 3.5 Graph State Object
```python
{
  "query": str,
  "retriever": object,
  "answer": str,
  "route": str
}
```
## 4. Workflow Design (LangGraph)

### Nodes
- `process Node`:
  - Takes user query
  - Calls retriever
  - Generates answer using LLM
  - Determines route (auto / escalate)
- `Output Node`:
  - Returns final response
  - Calls HITL if needed

### Edges
- Input → Process Node
- Process Node → Output Node

### State Flow
- Query → Retrieval → Answer → Routing → Output

## 5. Conditional Routing Logic

### Auto Answer Condition
- Relevant context is available
- LLM generates valid response

### Escalation Condition
- No context found
- Low confidence answer
- Complex query

### Routing Output
- "auto" → return generated answer
- "escalate" → trigger human response

## 6. HITL Design

### When Triggered
- No relevant chunks
- LLM cannot answer confidently
- Query is ambiguous

### Process
1. System detects escalation condition
2. Prompts human for input
3. Human provides response
4. Response returned to user

### Benefit
- Ensures reliability
- Prevents incorrect answers

## 7. API / Interface Design
`Input Format`
```python
{
  "query": "User question"
}
```
`Output Format`
```python
{
  "answer": "Final response",
  "route": "auto/escalate"
}
```
### Interaction Flow
1. User enters query
2. System processes via workflow
3. Response returned

## 8. Error Handling
### Missing Data
- Return fallback message
- No Relevant Chunks
- Trigger escalation
### LLM Failure
- Return safe fallback response
- Optionally escalate

## 9. Summary

The system is modular and structured, ensuring:

- Clear separation of responsibilities
- Easy debugging and scalability
- Reliable response generation with HITL fallback

This design enables efficient implementation of a production-style RAG system.