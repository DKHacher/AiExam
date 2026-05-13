from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from database.database import Base


class CardPrice(Base):
    __tablename__ = "card_prices"

    id = Column(Integer, primary_key=True, index=True)

    card_id = Column(
        Integer,
        ForeignKey("cards.card_id")
    )

    price_trend = Column(Float)

    price_low = Column(Float)

    available_quantity = Column(Integer)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )