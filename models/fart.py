from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import create_postgres_engine
from models.base import Base


class Fart(Base):
    __tablename__ = 'fart'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    url: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[int] = mapped_column(nullable=False)
    age_range: Mapped[int] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)


if __name__ == '__main__':
    engine = create_postgres_engine(echo=True)
    Base.metadata.create_all(engine)
