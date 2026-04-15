from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

#chromadb path
CHROMA_PATH="chroma_db"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
    )


def ingest_pdf(pdf_path:str):
    #step 1 -load the pdf
    print(f"Loading PDF: {pdf_path}")
    loader=PyPDFLoader(pdf_path)
    documents=loader.load()
    print(f"Loaded {len(documents)} documents")

    #step 2 -split the documents into chunks
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = splitter.split_documents(documents)
    print(f"Split {len(chunks)} chunks")

    #step 3 -chromadb store 
    print("Creating embeddings and storing in ChromaDB")
    vectorstore=Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=CHROMA_PATH,
    )
    print(f"Done! {len(chunks)} chunks stored in {CHROMA_PATH}")

    return len(chunks)


        