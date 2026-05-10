from pydantic import BaseModel

class ChatInputModel(BaseModel):
    message: str
    model: str