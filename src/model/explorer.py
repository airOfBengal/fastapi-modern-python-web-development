from pydantic import BaseModel, Field

class Explorer(BaseModel):
    name: str
    country: str
    description: str
    