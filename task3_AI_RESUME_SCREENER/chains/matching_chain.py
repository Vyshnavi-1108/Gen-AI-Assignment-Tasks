from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


def load_matching_chain():
    with open("prompts/matching.txt", "r", encoding="utf-8") as file:
        template = file.read()

    prompt = PromptTemplate.from_template(template)
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    parser = StrOutputParser()
    return prompt | llm | parser