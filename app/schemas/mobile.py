from pydantic import BaseModel


class MobileCreate(BaseModel):
    name: str
    price: float
    ram: str
    storage: str


class MobileResponse(MobileCreate):
    id: int

    class Config:
        from_attributes = True
