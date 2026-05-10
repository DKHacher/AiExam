from pydantic import BaseModel, Field
from datetime import datetime

class CardModel(BaseModel):
    id: int
    card_id: int
    name: str
    set_name: str
    rarity: str
    language: str
    price_trend: float
    price_low: float
    available_quantity: int
    updated_at: datetime
