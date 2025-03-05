from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

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
    score: Mapped[int] = mapped_column(nullable=False, default=0)
    number_of_votes: Mapped[int] = mapped_column(nullable=False, default=0)


if __name__ == '__main__':
    engine = create_postgres_engine(echo=True)
    Base.metadata.create_all(engine)
