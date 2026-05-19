from sqlalchemy.orm import Session

from models.databaseModels.carddbmodel import Card
from models.databaseModels.cardpricemodel import CardPrice

def get_all_cards(db: Session):
    return db.query(Card).all()


def get_card_by_id(db: Session, card_id: int):
    return db.query(Card).filter(Card.id == card_id).first()


def get_card_price_history(db: Session, card_id: int):
    return (
        db.query(CardPrice)
        .filter(CardPrice.card_id == card_id)
        .order_by(CardPrice.updated_at.asc())
        .all()
    )