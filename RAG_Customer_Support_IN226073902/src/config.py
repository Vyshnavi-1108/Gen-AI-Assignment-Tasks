import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PDF_PATH = "../data/sample.pdf"
DB_PATH = "db"
MODEL_NAME = "llama-3.1-8b-instant"