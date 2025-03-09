from typing import List

from fastapi import APIRouter, Query

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


@router.put('/')
async def update_fart_rating(db: DBDep, fart_id: int, new_score: int):
    return await services.fart.update_fart_rate(db=db, fart_id=fart_id, new_score=new_score)


@router.get('/')
async def get_farts(db: DBDep):
    return await services.fart.get_all_farts(db=db)


@router.get('/id/{fart_id}')
async def get_fart_by_id(db: DBDep, fart_id: int):
    return await services.fart.get_fart_by_id(db=db, fart_id=fart_id)


@router.get('/ranking')
async def get_farts_ranking(db: DBDep, page: int = 0, page_size: int = 20):
    return await services.fart.get_farts_by_score(db=db, page=page, page_size=page_size)


@router.get('/list')
async def get_farts_from_list(db: DBDep, farts_list: List[int] = Query([])):
    if not farts_list:
        return []
    return await services.fart.get_farts_list(db=db, fart_list=farts_list)



