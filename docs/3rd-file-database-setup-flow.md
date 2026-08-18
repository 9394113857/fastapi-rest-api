# Step 1️⃣ — Initialize Alembic:

# From the project root:
alembic init alembic


# Step 2️⃣ — Verify:
Get-ChildItem alembic

# Create database configuration:-
app/db/database.py

# Yep bro 😎🔥 easiest way — open it directly from your current PowerShell.

<!-- Run: -->
code .\alembic.ini

# 📱 Create app/models/mobile.py
New-Item -ItemType File -Force app\models\mobile.py | Out-Null

# Then open it:
code app\models\mobile.py

# Paste this full code:
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

-------------------------

# 🔄 Generate the migration
alembic revision --autogenerate -m "📱 create mobiles table"

# Now we do one thing only: inspect the migration before applying it. 🧐
Get-ChildItem alembic\versions

# 🔍 Now inspect that exact file:
Get-Content alembic\versions\dbb7494c2d73_create_mobiles_table.py

# 🚀 Next: APPLY the migration locally:
alembic upgrade head






