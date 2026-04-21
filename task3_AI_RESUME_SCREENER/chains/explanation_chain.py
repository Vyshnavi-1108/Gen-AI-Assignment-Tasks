from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


def load_explanation_chain():
    with open("prompts/explanation.txt", "r", encoding="utf-8") as file:
        template = file.read()

    prompt = PromptTemplate.from_template(template)
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    parser = StrOutputParser()
    return prompt | llm | parser