from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import crud.fart
import services.storage
from schemas.fart import FartCreate


async def add_fart(fart: FartCreate, db: AsyncSession):
    code, filename = services.storage.save_audio(fart.url)

    if code != 201:
        return None

    fart.url = filename
    fart = FartCreate(**fart.model_dump())
    return await crud.fart.create_fart(fart=fart, db=db)


async def get_all_farts(db: AsyncSession):
    return await crud.fart.get_farts_by_votes_asc(db)


async def get_fart_by_id(db: AsyncSession, fart_id: int):
    return await crud.fart.get_fart_by_id(db=db, fart_id=fart_id)


async def get_farts_by_score(db: AsyncSession, page: int = 0, page_size: int = 20):
    return await crud.fart.get_farts_by_score_desc(page=page, page_size=page_size, db=db)


async def get_farts_list(db: AsyncSession, fart_list: list[int]):
    return await crud.fart.get_farts_from_list(db=db, fart_list=fart_list)


async def update_fart_rate(db: AsyncSession, fart_id: int, new_score: int):
    db_fart = await crud.fart.get_fart_by_id(db=db, fart_id=fart_id)

    if not db_fart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fart not found"
        )

    return await crud.fart.update_rating(db=db, fart_id=fart_id, new_score=new_score)
