from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.mobile import Mobile
from app.schemas.mobile import MobileCreate


def get_all(db: Session):
    return db.scalars(select(Mobile)).all()


def get_by_id(db: Session, mobile_id: int):
    return db.get(Mobile, mobile_id)


def create(db: Session, data: MobileCreate):
    mobile = Mobile(**data.model_dump())

    db.add(mobile)
    db.commit()
    db.refresh(mobile)

    return mobile


def update(db: Session, mobile_id: int, data: MobileCreate):
    mobile = db.get(Mobile, mobile_id)

    if not mobile:
        return None

    for key, value in data.model_dump().items():
        setattr(mobile, key, value)

    db.commit()
    db.refresh(mobile)

    return mobile


def delete(db: Session, mobile_id: int):
    mobile = db.get(Mobile, mobile_id)

    if not mobile:
        return None

    db.delete(mobile)
    db.commit()

    return mobile
