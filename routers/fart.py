from fastapi import APIRouter

import services.fart
from dependencies import DBDep
from schemas.fart import FartCreate

router = APIRouter(
    prefix='/fart',
    tags=['fart'],
)


@router.post('/', response_model=bool)
async def add_fart(fart: FartCreate, db: DBDep):
    return bool(await services.fart.add_fart(fart=fart, db=db))


@router.get('/')
async def get_farts(db: DBDep):
    return await services.fart.get_all_farts(db=db)
