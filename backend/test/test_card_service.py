from database.database import SessionLocal
from tools.card_queries import get_all_cards

db = SessionLocal()

cards = get_all_cards(db)

for card in cards:
    print(card.name)