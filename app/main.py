from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from app.ingest import ingest_pdf
from app.chain import ask_question
import shutil
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="RAG Chatbot",
    description="Ask questions about your documents",
    version="1.0.0",
)

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

# Request model
class QuestionRequest(BaseModel):
    question: str

# ---routes----

@app.get("/")
def root():
    return {"message": "RAG Chatbot API is running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    file_path = os.path.join(DATA_PATH, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        chunks = ingest_pdf(file_path)
        return {
            "message": f"{file.filename} uploaded successfully",
            "chunks": chunks,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
async def ask(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        answer = ask_question(request.question)
        return {
            "question": request.question,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
