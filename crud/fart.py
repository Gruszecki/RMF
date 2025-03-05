from typing import Type

from sqlalchemy.orm import Session

import models.models
from schemas.fart import FartCreate


async def create_fart(db: Session, fart: FartCreate) -> models.models.Fart | None:
    db_fart = models.models.Fart(**fart.model_dump())
    if db_fart:
        db.add(db_fart)
        db.commit()
        db.refresh(db_fart)
        return db_fart
    return None


async def get_farts(db: Session) -> list[Type[models.models.Fart]]:
    return db.query(models.models.Fart).order_by(models.models.Fart.number_of_votes.asc()).all()
