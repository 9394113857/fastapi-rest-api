python -m pip install --upgrade pip

pip install fastapi uvicorn sqlalchemy alembic pydantic-settings

pip install "psycopg[binary]"

pip freeze > requirements.txt

pip list

Get-Content requirements.txt