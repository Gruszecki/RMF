from pydantic import BaseModel, Field
from typing import Annotated


class Fart(BaseModel):
    id: int
    url: str
    gender: Annotated[int, Field(ge=0, le=2)]
    age_range: Annotated[int, Field(ge=0, le=2)]
    country: str
