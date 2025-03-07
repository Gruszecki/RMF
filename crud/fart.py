from typing import Sequence

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.models import Fart
from schemas.fart import FartCreate


async def create_fart(db: AsyncSession, fart: FartCreate) -> Fart | None:
    db_fart = Fart(**fart.model_dump())
    if db_fart:
        db.add(db_fart)
        await db.commit()
        await db.refresh(db_fart)
        return db_fart
    return None


async def get_fart_by_id(db: AsyncSession, fart_id: int) -> Fart | None:
    result = await db.execute(select(Fart).where(Fart.id == fart_id))
    return result.scalar_one_or_none()


async def get_farts_by_votes_asc(db: AsyncSession) -> Sequence[Fart]:
    result = await db.execute(select(Fart).order_by(Fart.number_of_votes.asc()))
    return result.scalars().all()


async def update_rating(db: AsyncSession, fart_id: int, new_score: int) -> float:
    stmt = (
        update(Fart)
        .where(Fart.id == fart_id)
        .values(
            sum_votes=Fart.score_sum + new_score,
            num_votes=Fart.number_of_votes + 1
        )
        .returning(Fart.score_sum, Fart.number_of_votes)
    )

    result = await db.execute(stmt)
    sum_votes, num_votes = result.fetchone()

    await db.commit()

    return sum_votes / num_votes
