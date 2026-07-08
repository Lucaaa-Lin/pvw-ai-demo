from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from strands_pvw_agent import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://pvw-ai-demo.vercel.app",
        "https://pvw-ai-demo-eaul28thu-lucaaa-lins-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "PVW AI Agent backend is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = agent(request.message)
    return {"response": str(response)}