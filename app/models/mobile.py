from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Mobile(Base):
    __tablename__ = "mobiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    ram: Mapped[str] = mapped_column(String(50), nullable=False)
    storage: Mapped[str] = mapped_column(String(50), nullable=False)
