from datetime import datetime
from pydantic import BaseModel


class CardPriceResponse(BaseModel):
    id: int
    card_id: int
    price: float
    available_items: int
    updated_at: datetime

    class Config:
        from_attributes = True