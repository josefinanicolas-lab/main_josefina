from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from app.config import LOCAL_AUTH_TOKEN
from app.services.openai_client import ask_openai

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    context: dict | None = None

@router.get("/health")
def health():
    return {"ok": True}

@router.post("/chat")
def chat(req: ChatRequest, authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Authorization Bearer token")

    token = authorization.removeprefix("Bearer ").strip()
    if token != LOCAL_AUTH_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    reply = ask_openai(req.message, req.context)
    return {"reply": reply}
