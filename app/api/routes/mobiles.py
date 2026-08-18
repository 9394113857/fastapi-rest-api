from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.mobile import MobileCreate, MobileResponse
from app.services import mobile as mobile_service

router = APIRouter(
    prefix="/mobiles",
    tags=["Mobiles"],
)


@router.get("/", response_model=list[MobileResponse])
def get_mobiles(db: Session = Depends(get_db)):
    return mobile_service.get_all(db)


@router.get("/{mobile_id}", response_model=MobileResponse)
def get_mobile(mobile_id: int, db: Session = Depends(get_db)):
    mobile = mobile_service.get_by_id(db, mobile_id)

    if not mobile:
        raise HTTPException(
            status_code=404,
            detail="Mobile not found",
        )

    return mobile


@router.post("/", response_model=MobileResponse, status_code=201)
def create_mobile(
    data: MobileCreate,
    db: Session = Depends(get_db),
):
    return mobile_service.create(db, data)


@router.put("/{mobile_id}", response_model=MobileResponse)
def update_mobile(
    mobile_id: int,
    data: MobileCreate,
    db: Session = Depends(get_db),
):
    mobile = mobile_service.update(db, mobile_id, data)

    if not mobile:
        raise HTTPException(
            status_code=404,
            detail="Mobile not found",
        )

    return mobile


@router.delete("/{mobile_id}")
def delete_mobile(
    mobile_id: int,
    db: Session = Depends(get_db),
):
    mobile = mobile_service.delete(db, mobile_id)

    if not mobile:
        raise HTTPException(
            status_code=404,
            detail="Mobile not found",
        )

    return {"message": "Mobile deleted successfully"}
