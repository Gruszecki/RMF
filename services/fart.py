from sqlalchemy.orm import Session

from crud.fart import create_fart, get_farts
from schemas.fart import FartCreate


async def add_fart(fart: FartCreate, db: Session):
    fart = FartCreate(**fart.model_dump())
    return await create_fart(fart=fart, db=db)


async def get_all_farts(db: Session):
    return await get_farts(db)
