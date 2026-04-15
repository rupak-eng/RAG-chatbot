from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

# Path to the data directory
CHROMA_PATH = "chroma_db"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
    )

def get_retriever():
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings(),
    )
    return vectorstore.as_retriever(search_kwargs={"k": 5})

def get_relevant_chunks(query:str):
    retriever = get_retriever()
    docs = retriever.invoke(query)
    return docs

