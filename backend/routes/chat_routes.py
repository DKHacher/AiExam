from fastapi import APIRouter
from models.apiModels.ChatInputModel import ChatInputModel
from models.apiModels.ChatOutputModel import ChatOutputModel
from services.llm_service import ask_llm

router = APIRouter()


@router.post("/chat", response_model=ChatOutputModel)
async def chat(request: ChatInputModel):
    return ChatOutputModel(
        response=ask_llm(request.message, request.model)
    )