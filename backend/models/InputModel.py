from pydantic import BaseModel, Field

class InputModel(BaseModel):
    input: str
    model: str