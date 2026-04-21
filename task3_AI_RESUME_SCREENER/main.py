import os
from dotenv import load_dotenv
from chains.skill_extraction_chain import load_skill_extraction_chain
from chains.matching_chain import load_matching_chain
from chains.scoring_chain import load_scoring_chain
from chains.explanation_chain import load_explanation_chain


def read_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def save_output(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def run_pipeline(resume_path, job_description_path):
    resume_text = read_text(resume_path)
    job_description = read_text(job_description_path)

    skill_chain = load_skill_extraction_chain()
    matching_chain = load_matching_chain()
    scoring_chain = load_scoring_chain()
    explanation_chain = load_explanation_chain()

    candidate_profile = skill_chain.invoke({"resume_text": resume_text})
    matching_report = matching_chain.invoke(
        {
            "job_description": job_description,
            "candidate_profile": candidate_profile,
        }
    )
    score_output = scoring_chain.invoke(
        {
            "job_description": job_description,
            "matching_report": matching_report,
        }
    )
    explanation = explanation_chain.invoke(
        {
            "job_description": job_description,
            "candidate_profile": candidate_profile,
            "matching_report": matching_report,
            "score_output": score_output,
        }
    )

    result = []
    result.append("=" * 80)
    result.append(f"Resume File: {resume_path}")
    result.append("=" * 80)
    result.append("\nSTEP 1: SKILL EXTRACTION\n")
    result.append(candidate_profile)
    result.append("\nSTEP 2: MATCHING\n")
    result.append(matching_report)
    result.append("\nSTEP 3: SCORING\n")
    result.append(score_output)
    result.append("\nSTEP 4: EXPLANATION\n")
    result.append(explanation)
    result.append("\n")
    return "\n".join(result)


def main():
    load_dotenv()

    required_vars = ["GROQ_API_KEY", "LANGCHAIN_API_KEY"]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise ValueError(
            "Missing environment variables: " + ", ".join(missing) +
            ". Copy .env.example to .env and fill the values."
        )

    job_description_path = "data/job_description.txt"
    resume_files = [
        "data/resume_strong.txt",
        "data/resume_average.txt",
        "data/resume_weak.txt",
    ]

    all_results = []
    for resume_file in resume_files:
        result = run_pipeline(resume_file, job_description_path)
        print(result)
        all_results.append(result)

    save_output("results.txt", "\n\n".join(all_results))
    print("\nSaved final output to results.txt")


if __name__ == "__main__":
    main()
