from config import PDF_PATH
from ingestion import load_and_chunk_pdf
from retrieval import create_vector_store, get_retriever
from workflow import build_graph


def main():
    print("📄 Loading PDF...")
    chunks = load_and_chunk_pdf(PDF_PATH)

    print("🧠 Creating vector database...")
    vectordb = create_vector_store(chunks)

    retriever = get_retriever(vectordb)

    print("🔁 Building workflow...")
    app = build_graph()

    print("\n✅ Customer Support Assistant Ready")

    while True:
        query = input("\nAsk a question (type exit to quit): ")

        if query.lower() == "exit":
            break

        result = app.invoke({
            "query": query,
            "retriever": retriever,
            "answer": "",
            "route": ""
        })

        print("\n💬 Answer:", result["answer"])


if __name__ == "__main__":
    main()