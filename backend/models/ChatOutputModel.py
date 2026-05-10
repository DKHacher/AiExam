from pydantic import BaseModel, Field


class ChatOutputModel(BaseModel):
    response : str = Field(..., description="The response from the LLM")