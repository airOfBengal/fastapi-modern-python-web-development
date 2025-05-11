from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

