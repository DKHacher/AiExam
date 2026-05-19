from database.database import Base
from models.databaseModels.carddbmodel import Card
from models.databaseModels.cardpricemodel import CardPrice

print(Base.metadata.tables.keys())