from sqlalchemy.orm import Session

from app.repositories import mobile as mobile_repository
from app.schemas.mobile import MobileCreate


def get_all(db: Session):
    return mobile_repository.get_all(db)


def get_by_id(db: Session, mobile_id: int):
    return mobile_repository.get_by_id(db, mobile_id)


def create(db: Session, data: MobileCreate):
    return mobile_repository.create(db, data)


def update(db: Session, mobile_id: int, data: MobileCreate):
    return mobile_repository.update(db, mobile_id, data)


def delete(db: Session, mobile_id: int):
    return mobile_repository.delete(db, mobile_id)
