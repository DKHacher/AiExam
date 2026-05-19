from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from services.card_service import (
    get_all_cards,
    get_card_by_id,
    get_card_price_history
)
from fastapi.middleware.cors import CORSMiddleware

from routes.chat_routes import router as chat_router

from schemas.card_schema import CardResponse
from schemas.card_price_schema import CardPriceResponse

from typing import List

app = FastAPI(
    title="AI Trading Card Predictor",
    description="AI powered trading card market analysis API",
    version="0.1.0"
)

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change later if i change to a deployed state, for now its fine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat_router)

# Root route
@app.get("/")
def root():
    return {
        "message": "Backend is running"
    }

# Health check route
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


#api routes
@app.get("/cards", response_model=List[CardResponse])
def read_cards(db: Session = Depends(get_db)):
    return get_all_cards(db)

@app.get("/cards/{card_id}", response_model=CardResponse)
def read_card(card_id: int, db: Session = Depends(get_db)):
    return get_card_by_id(db, card_id)

@app.get(
    "/cards/{card_id}/history",
    response_model=List[CardPriceResponse]
)
def read_card_history(card_id: int, db: Session = Depends(get_db)):
    return get_card_price_history(db, card_id)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )



