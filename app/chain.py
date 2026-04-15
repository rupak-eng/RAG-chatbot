from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.retriever import get_retriever
from dotenv import load_dotenv
import os

load_dotenv()

#prompt template -instructions for the llm
PROMPT_TEMPLATE = """
you are a helpful assistant that answers questions based on the context provided.
if the answer is not in the context, say "I don't know"

Context:
{context}

Question:
{question}

Answer:
"""

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_rag_chain():
    llm=ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.1,
        api_key=os.getenv("GROQ_API_KEY"),
    )
    prompt=ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    
    chain=(
        {
            "context":get_retriever()|format_docs,
            "question":RunnablePassthrough(),
        }
        |prompt
        |llm
        |StrOutputParser()
    )
    return chain

def ask_question(question:str)->str:
    chain=get_rag_chain()
    return chain.invoke(question)
    