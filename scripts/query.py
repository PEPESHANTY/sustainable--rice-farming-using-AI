# scripts/query.py

from dotenv import load_dotenv
load_dotenv()

from scripts.utils import save_chat_history

from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

import pathlib
VECTOR_DIR = str(pathlib.Path(__file__).resolve().parent.parent / "vectorstore")


# Load vector store
db = FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

# Prompt template
template = """You are a helpful AI assistant supporting rice farmers in sustainable practices.
Use the provided context to answer the question. If unsure, reason based on your knowledge and cite relevant sources.
If the user requests a response in a specific language, respond in that language.

Context:
{context}

Question:
{question}

Helpful Answer:"""

prompt = PromptTemplate(input_variables=["context", "question"], template=template)

# QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    retriever=db.as_retriever(search_kwargs={"k": 6}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

# 🔁 Function for use in app.py
def get_response_from_chain(user_query, chat_history):
    context_query = "\n".join(chat_history + [f"User: {user_query}"])
    result = qa_chain.invoke(context_query)
    return result["result"], result["source_documents"]

# 🧪 CLI mode for testing
if __name__ == "__main__":
    chat_history = []

    while True:
        query = input("\nAsk a question about rice farming (or type 'exit'): ")
        if query.lower() in ["exit", "save chat", "bye now", "bye"]:
            break

        response, sources = get_response_from_chain(query, chat_history)

        print("\n🔍 Answer:")
        print(response)

        print("\n📚 Sources:")

        unique_sources = set(doc.metadata.get("source", "Unknown") for doc in sources)
        for src in sorted(unique_sources):
            print("—", src)

        chat_history.append(f"User: {query}")
        chat_history.append(f"AI: {response}")

    # Save history
    chat_log = []
    for entry in chat_history:
        role = "user" if entry.startswith("User:") else "assistant"
        content = entry.split(":", 1)[1].strip()
        chat_log.append({"role": role, "content": content})

    save_chat_history(chat_log)
