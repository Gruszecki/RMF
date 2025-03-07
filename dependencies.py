from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


DBDep = Annotated[AsyncSession, Depends(get_db)]
