from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
import secrets_handler


def create_postgres_engine(echo=False) -> Engine:
    db = f'postgresql+psycopg2://{secrets_handler.DB_USERNAME}:{secrets_handler.DB_PASSWORD}@' \
         f'{secrets_handler.DB_HOSTNAME}:{secrets_handler.DB_PORT}/{secrets_handler.DB_DATABASE}'
    return create_engine(db, echo=echo)


engine = create_postgres_engine(echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    with Session(engine) as session:
        result = session.execute(text('select version()'))
        print(result.all())
