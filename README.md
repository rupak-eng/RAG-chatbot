# 🤖 RAG Chatbot

A high-performance Retrieval-Augmented Generation (RAG) chatbot built with **FastAPI**, **LangChain**, and **Groq**. This application allows you to upload PDF documents and ask questions about their content using state-of-the-art LLMs (Llama 3.3).

## 🚀 Features

- **PDF Ingestion**: Upload documents via API; they are automatically split into chunks and indexed.
- **RAG Architecture**: Uses semantic search to retrieve relevant context before generating answers.
- **Fast Inference**: Powered by **Groq** for lightning-fast responses.
- **Vector Storage**: Uses **ChromaDB** for efficient document storage and retrieval.
- **REST API**: Built with FastAPI for easy integration with frontend applications.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **LLM**: [Groq](https://groq.com/) (Llama-3.3-70b-versatile)
- **Embeddings**: [Hugging Face](https://huggingface.co/) (all-MiniLM-L6-v2)
- **Vector DB**: [ChromaDB](https://www.trychroma.com/)

## 🚦 Getting Started

### 1. Prerequisites
- Python 3.14+
- A Groq API Key ([Get it here](https://console.groq.com/))

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
```

Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
# OR if using uv
uv sync
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_api_key_here
```

### 4. Running the Application
Start the FastAPI server:
```bash
uvicorn app.main:app --reload --port 8000
```

## 📡 API Endpoints

- **GET `/`**: Check if the API is running.
- **POST `/upload`**: Upload a PDF file for indexing.
- **POST `/ask`**: Send a question to the chatbot.
  - Body: `{"question": "What is the summary of the document?"}`
- **GET `/health`**: Check system status.

## 📁 Project Structure

```text
rag-chatbot/
├── app/
│   ├── __init__.py
│   ├── ingest.py      # PDF processing & indexing
│   ├── retriever.py   # Vector search logic
│   ├── chain.py       # RAG chain implementation
│   └── main.py        # FastAPI routes
├── data/              # Storage for uploaded PDFs (ignored by git)
├── chroma_db/         # Local vector database (ignored by git)
├── .env               # API keys (ignored by git)
├── .gitignore
└── README.md
```

## 📝 License
MIT License
# RAG-chatbot
