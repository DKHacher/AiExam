from pydantic import BaseModel


class CardResponse(BaseModel):
    id: int
    name: str
    set_name: str
    rarity: str

    class Config:
        from_attributes = True