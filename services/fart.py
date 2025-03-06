from sqlalchemy.orm import Session

import services.storage
from crud.fart import create_fart, get_farts_by_votes_asc
from schemas.fart import FartCreate


async def add_fart(fart: FartCreate, db: Session):
    code, filename = services.storage.save_audio(fart.url)

    if code != 201:
        return None

    fart.url = filename
    fart = FartCreate(**fart.model_dump())
    return await create_fart(fart=fart, db=db)


async def get_all_farts(db: Session):
    return await get_farts_by_votes_asc(db)
