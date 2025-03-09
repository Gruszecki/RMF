from typing import Sequence

from sqlalchemy import case, func, update
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


async def get_farts_from_list(db: AsyncSession, fart_list: list[int]) -> Sequence[Fart] | None:
    result = await db.execute(select(Fart).where(Fart.id.in_(fart_list)).order_by(Fart.id.asc()))
    return result.scalars().all()


async def get_farts_by_votes_asc(db: AsyncSession) -> Sequence[Fart] | None:
    result = await db.execute(select(Fart).order_by(Fart.number_of_votes.asc()))
    return result.scalars().all()


async def get_farts_by_score_desc(db: AsyncSession, page: int = 0, page_size: int = 20) -> Sequence[Fart] | None:
    offset = page * page_size

    result = await db.execute(
        select(Fart)
        .order_by(
            (Fart.score_sum / case(
                (Fart.number_of_votes == 0, 1),
                else_=Fart.number_of_votes
            )).desc()
        )
        .offset(offset)
        .limit(page_size)
    )
    return result.scalars().all()


async def update_rating(db: AsyncSession, fart_id: int, new_score: int) -> float:
    stmt = (
        update(Fart)
        .where(Fart.id == fart_id)
        .values(
            score_sum=Fart.score_sum + new_score,
            number_of_votes=Fart.number_of_votes + 1
        )
        .returning(Fart.score_sum, Fart.number_of_votes)
    )

    result = await db.execute(stmt)
    sum_votes, num_votes = result.fetchone()

    await db.commit()

    return sum_votes / num_votes
