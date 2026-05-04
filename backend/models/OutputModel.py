from pydantic import BaseModel, Field


class OutputModel(BaseModel):
    response : str = Field(..., description="The response from the LLM")