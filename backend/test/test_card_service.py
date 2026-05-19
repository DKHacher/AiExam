from database.database import SessionLocal
from services.card_service import get_all_cards

db = SessionLocal()

cards = get_all_cards(db)

for card in cards:
    print(card.name)