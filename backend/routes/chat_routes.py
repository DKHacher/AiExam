from fastapi import APIRouter

from models.ChatInputModel import ChatInputModel
from models.ChatOutputModel import ChatOutputModel

from services.llm_service import ask_llm

router = APIRouter()

@router.post("/chat", response_model=ChatOutputModel)
async def chat(request: ChatInputModel):

    response = ask_llm(request.message)

    return ChatOutputModel(
        response=response
    )