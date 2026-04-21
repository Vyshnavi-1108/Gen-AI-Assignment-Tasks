# AI Resume Screening System with LangChain, Groq, and LangSmith

This project is a complete internship assignment solution for building an AI Resume Screening System.
It uses LangChain for the modular pipeline, Groq as the free LLM API provider, and LangSmith for tracing.

## Features
- Resume skill extraction
- Resume and job description matching
- Candidate scoring from 0 to 100
- Human-readable explanation
- LangSmith tracing for all runs
- Three sample resumes: strong, average, weak

## Tech Stack
- Python
- LangChain
- Groq API
- LangSmith

## Project Structure
```text
ai-resume-screening-system/
├── prompts/
├── chains/
├── data/
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file by copying `.env.example`.

Windows:
```bash
copy .env.example .env
```

Mac/Linux:
```bash
cp .env.example .env
```

5. Fill your keys in `.env`.

## Free API Note
This project is designed to use Groq so you can avoid OpenAI billing. You still need your own free Groq API key and LangSmith key.

## Run the Project
```bash
python main.py
```

## Output
The script prints results for all three resumes and saves them to `results.txt`.

## LangSmith Tracing
Make sure these are set in `.env`:
```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=ai-resume-screening-system
```

Run the script and check your LangSmith dashboard for three traces.

## Suggested GitHub Steps
```bash
git init
git add .
git commit -m "Initial commit"
```

Then create a GitHub repository and push your code.

## Suggested LinkedIn Post Idea
Built an AI Resume Screening System using LangChain, Groq, and LangSmith. The pipeline extracts skills, matches resumes with the job description, assigns a score, and explains the result with full tracing.
