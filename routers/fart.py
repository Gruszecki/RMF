from fastapi import APIRouter

import services.fart
from dependencies import DBDep
from schemas.fart import FartCreate

router = APIRouter(
    prefix='/fart',
    tags=['fart'],
)


@router.post('/')
async def add_fart(db: DBDep, fart: FartCreate):
    return await services.fart.add_fart(fart=fart, db=db)


@router.get('/')
async def get_farts(db: DBDep):
    return await services.fart.get_all_farts(db=db)


@router.put('/')
async def update_fart_rating(db: DBDep, fart_id: int, new_score: int):
    return await services.fart.update_fart_rate(db=db, fart_id=fart_id, new_score=new_score)
