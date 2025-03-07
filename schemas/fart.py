from pydantic import BaseModel, Field
from typing import Annotated


class FartBase(BaseModel):
    pass


class Fart(FartBase):
    id: int
    score_sum: Annotated[int, Field(default=0)]
    number_of_votes: Annotated[int, Field(default=0)]

    class Config:
        from_attributes = True


class FartCreate(FartBase):
    url: str
    gender: Annotated[int, Field(ge=0, le=2)]
    age_range: Annotated[int, Field(ge=0, le=2)]
    country: str
