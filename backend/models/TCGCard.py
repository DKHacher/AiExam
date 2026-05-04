from pydantic import BaseModel, Field

class TCGCard(BaseModel):
    id: int
    card_id: int
    name: str
    price_trend: float
    price_low: float
    date: datetime
