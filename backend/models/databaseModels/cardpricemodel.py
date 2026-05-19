from sqlalchemy import *
from datetime import datetime

from database.database import Base

class CardPrice(Base):
    __tablename__ = "card_prices"

    id = Column(Integer, primary_key=True)

    card_id = Column(Integer, ForeignKey("cards.id"))

    price = Column(Float, nullable=False)
    available_items = Column(Integer, nullable=False)

    is_foil = Column(Integer, default=0)  # or Boolean
    condition = Column(String, default="NM")  # Near Mint, etc
    language = Column(String, default="English")

    is_signed = Column(Integer, default=0)
    is_altered = Column(Integer, default=0)

    updated_at = Column(DateTime, default=datetime.utcnow)