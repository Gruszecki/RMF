from pydantic import BaseModel, Field
from typing import Annotated


class FartBase(BaseModel):
    url: str
    gender: Annotated[int, Field(ge=0, le=2)]
    age_range: Annotated[int, Field(ge=0, le=2)]
    country: str
    score: Annotated[int, Field(ge=0, le=100)]
    number_of_votes: Annotated[int, Field(ge=0)]


class Fart(FartBase):
    id: int

    class Config:
        from_attributes = True


class FartCreate(FartBase):
    pass
