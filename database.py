import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import text

import secrets_handler


def create_postgres_engine(echo=False):
    db = f'postgresql+asyncpg://{secrets_handler.DB_USERNAME}:{secrets_handler.DB_PASSWORD}@' \
         f'{secrets_handler.DB_HOSTNAME}:{secrets_handler.DB_PORT}/{secrets_handler.DB_DATABASE}'
    return create_async_engine(db, echo=echo)


engine = create_postgres_engine(echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=AsyncSession)


async def main():
    async with AsyncSessionLocal() as session:
        result = await session.execute(text('select version()'))
        print(result.fetchall())


if __name__ == '__main__':
    asyncio.run(main())
