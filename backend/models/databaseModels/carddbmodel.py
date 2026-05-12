from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)

    card_id = Column(Integer, unique=True)

    name = Column(String)

    set_name = Column(String)

    rarity = Column(String)

    language = Column(String)

    price_trend = Column(Float)

    price_low = Column(Float)

    available_quantity = Column(Integer)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )