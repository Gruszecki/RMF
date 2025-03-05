from fastapi import APIRouter

import services.fart
from dependencies import DBDep
from schemas.fart import Fart

router = APIRouter(
    prefix='/fart',
    tags=['fart'],
)


@router.post('/', response_model=bool)
async def add_fart(fart: Fart, db: DBDep):
    return bool(await services.fart.add_fart(fart=fart, db=db))
