from sqlalchemy.orm import Session

import models.fart
from schemas.fart import Fart


def create_fart(db: Session, fart: Fart) -> models.fart.Fart | None:
    db_fart = models.fart.Fart(**fart.model_dump())
    if db_fart:
        db.add(db_fart)
        db.commit()
        db.refresh(db_fart)
        return db_fart
    return None
