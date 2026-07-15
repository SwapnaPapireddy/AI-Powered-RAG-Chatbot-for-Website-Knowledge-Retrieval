from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.request import URLRequest, ChatRequest
from models.response import WebsiteResponse, ChatResponse

from crawler.loader import WebsiteLoader
from crawler.splitter import DocumentSplitter

from embeddings.embedding_model import EmbeddingModel
from embeddings.vector_store import VectorStore

from chatbot.retriever import Retriever
from chatbot.rag_pipeline import RAGPipeline

from config.settings import Settings

# -------------------------------
# FastAPI App
# -------------------------------

app = FastAPI(
    title="Website RAG Chatbot",
    version="1.0"
)

# -------------------------------
# CORS
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Global Variables
# -------------------------------

rag_pipeline = None
website_loaded = False

# -------------------------------
# Home
# -------------------------------

@app.get("/")
def home():
    return {
        "message": "Website RAG Chatbot API Running"
    }

# -------------------------------
# Load Website
# -------------------------------

@app.post(
    "/load",
    response_model=WebsiteResponse
)
def load_website(request: URLRequest):

    global rag_pipeline
    global website_loaded

    try:

        # Load Website
        loader = WebsiteLoader(str(request.url))
        documents = loader.load()

        # Split Documents
        splitter = DocumentSplitter(
            chunk_size=Settings.CHUNK_SIZE,
            chunk_overlap=Settings.CHUNK_OVERLAP
        )

        chunks = splitter.split_documents(documents)

        # Embeddings
        embedding_model = EmbeddingModel()

        embeddings = embedding_model.load()

        # Vector Store
        vector_store = VectorStore(embeddings)

        db = vector_store.create_vector_store(chunks)

        vector_store.save_vector_store(
            db,
            Settings.VECTOR_DB_PATH
        )

        # Retriever
        retriever = Retriever(db).get_retriever()

        # RAG Pipeline
        rag_pipeline = RAGPipeline(retriever)

        website_loaded = True

        return WebsiteResponse(
            status="Success",
            message="Website processed successfully.",
            documents_loaded=len(documents),
            chunks_created=len(chunks)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# -------------------------------
# Chat
# -------------------------------

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    global rag_pipeline
    global website_loaded

    if not website_loaded:

        raise HTTPException(
            status_code=400,
            detail="Please load a website first."
        )

    try:

        answer = rag_pipeline.ask(
            request.question
        )

        return ChatResponse(
            question=request.question,
            answer=answer
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# -------------------------------
# Reset Conversation
# -------------------------------

@app.post("/reset")
def reset_chat():

    global rag_pipeline

    if rag_pipeline:

        rag_pipeline.reset_chat()

    return {
        "message": "Conversation cleared successfully."
    }

# -------------------------------
# Health Check
# -------------------------------

@app.get("/health")
def health():

    return {
        "status": "OK",
        "website_loaded": website_loaded
    }