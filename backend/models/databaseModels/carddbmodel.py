from sqlalchemy import *
from database.database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True, nullable=False)
    set_name = Column(String, nullable=False)
    rarity = Column(String, nullable=False)
    language = Column(String, nullable=False)