from groq import Groq
from dotenv import load_dotenv
import os
from config import MODEL_NAME

# Load environment variables
load_dotenv()

# Get API key safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def generate_answer(retriever, query):
    # Retrieve relevant documents
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    # If no context found
    if not context.strip():
        return "I don't know"

    # Prompt
    prompt = f"""
You are a customer support assistant.

Answer ONLY from the given context.
If the answer is not available, reply exactly:
I don't know

Context:
{context}

Question:
{query}
"""

    # LLM call
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()