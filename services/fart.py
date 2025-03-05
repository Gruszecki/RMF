from sqlalchemy.orm import Session

from crud.fart import create_fart
from schemas.fart import FartCreate


async def add_fart(fart: FartCreate, db: Session):
    fart = FartCreate(**fart.model_dump())
    return create_fart(fart=fart, db=db)
