from sqlalchemy.orm import Session

import models.models
from schemas.fart import FartCreate


def create_fart(db: Session, fart: FartCreate) -> models.models.Fart | None:
    db_fart = models.models.Fart(**fart.model_dump())
    if db_fart:
        db.add(db_fart)
        db.commit()
        db.refresh(db_fart)
        return db_fart
    return None
