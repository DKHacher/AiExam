from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat_routes import router as chat_router

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