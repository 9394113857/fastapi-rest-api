from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes.mobiles import router as mobile_router

app = FastAPI(
    title="FastAPI REST API",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


app.include_router(mobile_router)


@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}
