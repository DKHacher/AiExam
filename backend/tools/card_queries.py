from langchain.tools import tool
from database.database import SessionLocal
from models.databaseModels.carddbmodel import Card
from models.databaseModels.cardpricemodel import CardPrice

@tool
def get_all_cards():
    """
    Get all trading cards in the database.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        cards = db.query(Card).all()

        if not cards:
            return {
                "success": False,
                "error": "No cards found",
                "data": []
            }

        return {
            "success": True,
            "count": len(cards),
            "data": [
                {
                    "id": card.id,
                    "name": card.name,
                    "set_name": card.set_name,
                    "rarity": card.rarity,
                    "language": card.language
                }
                for card in cards
            ]
        }

    finally:
        db.close()

@tool
def get_card_by_id(card_id: int):
    """
    Get a single trading card by its ID.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        card = db.query(Card).filter(Card.id == card_id).first()

        if not card:
            return {
                "success": False,
                "error": "Card not found",
                "data": None
            }

        return {
            "success": True,
            "data": {
                "id": card.id,
                "name": card.name,
                "set_name": card.set_name,
                "rarity": card.rarity,
                "language": card.language
            }
        }

    finally:
        db.close()

@tool
def get_card_by_name(card_name: str):
    """
    Get a single trading card by its Name.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        card = (
            db.query(Card)
            .filter(Card.name.ilike(f"%{card_name}%"))
            .first()
        )

        if not card:
            return {
                "success": False,
                "error": "Card not found",
                "data": None
            }

        return {
            "success": True,
            "data": {
                "id": card.id,
                "name": card.name,
                "set_name": card.set_name,
                "rarity": card.rarity,
                "language": card.language
            }
        }

    finally:
        db.close()

@tool
def get_price_history_by_card_id(card_id: int):
    """
    Get full price history for a card using its ID.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        history = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card_id)
            .order_by(CardPrice.updated_at.asc())
            .all()
        )

        if not history:
            return {
                "success": False,
                "error": "No price history found",
                "data": None
            }

        return {
            "success": True,
            "card_id": card_id,
            "data": [
                {
                    "date": str(entry.updated_at),
                    "price": entry.price,
                    "available_items": entry.available_items
                }
                for entry in history
            ]
        }

    finally:
        db.close()

@tool
def get_price_history_by_card_name(card_name: str):
    """
    Get full price history for a card using its name (partial match supported).
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        card = (
            db.query(Card)
            .filter(Card.name.ilike(f"%{card_name}%"))
            .first()
        )

        if not card:
            return {
                "success": False,
                "error": "Card not found",
                "data": None
            }

        history = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card.id)
            .order_by(CardPrice.updated_at.asc())
            .all()
        )

        if not history:
            return {
                "success": False,
                "error": "No price history found",
                "data": None
            }

        return {
            "success": True,
            "card": {
                "id": card.id,
                "name": card.name
            },
            "data": [
                {
                    "date": str(entry.updated_at),
                    "price": entry.price,
                    "available_items": entry.available_items
                }
                for entry in history
            ]
        }

    finally:
        db.close()

@tool
def get_latest_price_for_card_by_id(card_id: int):
    """
    Get the most recent price entry for a card by its id.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        latest = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card_id)
            .order_by(CardPrice.updated_at.desc())
            .first()
        )

        if not latest:
            return {
                "success": False,
                "error": "No price found",
                "data": None
            }

        return {
            "success": True,
            "card_id": card_id,
            "data": {
                "date": str(latest.updated_at),
                "price": latest.price,
                "available_items": latest.available_items
            }
        }

    finally:
        db.close()

@tool
def get_latest_price_for_card_by_name(card_name: str):
    """
    Get the most recent price entry for a card by its id.
    Returns a structured JSON response.
    """
    db = SessionLocal()

    try:
        card = (
            db.query(Card)
            .filter(Card.name.ilike(f"%{card_name}%"))
            .first()
        )

        if not card:
            return {
                "success": False,
                "error": "Card not found",
                "data": None
            }

        latest = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card.id)
            .order_by(CardPrice.updated_at.desc())
            .first()
        )

        if not latest:
            return {
                "success": False,
                "error": "No price found",
                "data": None
            }

        return {
            "success": True,
            "card_id": card.id,
            "data": {
                "date": str(latest.updated_at),
                "price": latest.price,
                "available_items": latest.available_items
            }
        }

    finally:
        db.close()

@tool
def analyze_price_trend_by_card_id(card_id: int):
    """
    Analyze whether a card is rising, falling, or stable based on price history.
    Finds a card in the database by Id.
    Returns structured JSON with trend and percentage change.
    """

    db = SessionLocal()

    try:
        history = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card_id)
            .order_by(CardPrice.updated_at.asc())
            .all()
        )

        if not history:
            return {
                "success": False,
                "error": "No price history found",
                "data": None
            }

        if len(history) < 2:
            return {
                "success": False,
                "error": "Too few price history entries to calculate trend",
                "data": None
            }

        start_price = history[0].price
        end_price = history[-1].price

        percent_change = ((end_price - start_price) / start_price) * 100

        if percent_change > 5:
            trend = "rising"
        elif percent_change < -5:
            trend = "falling"
        else:
            trend = "stable"

        return {
            "card_id": card_id,
            "trend": trend,
            "percent_change": round(percent_change, 2),
            "start_price": start_price,
            "end_price": end_price,
            "data_points": len(history)
        }

    finally:
        db.close()

@tool
def analyze_price_trend_by_name(card_name: str):
    """
    Analyze whether a card is rising, falling, or stable based on price history.
    Finds a card in the database by name.
    Returns structured JSON with trend and percentage change.
    """

    db = SessionLocal()

    try:
        card = (
            db.query(Card)
            .filter(Card.name.ilike(f"%{card_name}%"))
            .first()
        )

        if not card:
            return {
                "success": False,
                "error": "Card not found",
                "data": None
            }

        history = (
            db.query(CardPrice)
            .filter(CardPrice.card_id == card.id)
            .order_by(CardPrice.updated_at.asc())
            .all()
        )

        if not history:
            return {
                "success": False,
                "error": "No price history found",
                "data": None
            }

        if len(history) < 2:
            return {
                "success": False,
                "error": "Too few price history entries to calculate trend",
                "data": None
            }

        start = history[0].price
        end = history[-1].price

        pct = ((end - start) / start) * 100

        if pct > 5:
            trend = "rising"
        elif pct < -5:
            trend = "falling"
        else:
            trend = "stable"

        return {
            "card": {
                "id": card.id,
                "name": card.name
            },
            "trend": trend,
            "percent_change": round(pct, 2),
            "data_points": len(history)
        }

    finally:
        db.close()