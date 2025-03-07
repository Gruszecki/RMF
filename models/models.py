from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio

from database import create_postgres_engine


class Base(DeclarativeBase):
    pass


class Fart(Base):
    __tablename__ = 'fart'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False, autoincrement=True)
    url: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[int] = mapped_column(nullable=False)
    age_range: Mapped[int] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    score_sum: Mapped[int] = mapped_column(nullable=False, default=0)
    number_of_votes: Mapped[int] = mapped_column(nullable=False, default=0)


engine = create_postgres_engine(echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=AsyncSession)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await create_tables()


if __name__ == '__main__':
    asyncio.run(main())
