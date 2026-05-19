from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.apiModels.ChatInputModel import ChatInputModel
from models.apiModels.ChatOutputModel import ChatOutputModel
from services.card_service import get_card_by_name, get_card_price_history

from services.llm_service import ask_llm

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatInputModel, db: Session = Depends(get_db)):

    card = get_card_by_name(db, request.message)

    history = get_card_price_history(db, card.id)

    response = ask_llm(
        request.message,
        str(history)
    )

    return ChatOutputModel(response=response)