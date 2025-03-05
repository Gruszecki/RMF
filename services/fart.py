from sqlalchemy.orm import Session

from crud.fart import create_fart
from schemas.fart import Fart


async def add_fart(fart: Fart, db: Session):
    fart = Fart(**fart.model_dump())
    return create_fart(fart=fart, db=db)
