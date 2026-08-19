import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes.mobiles import router as mobile_router


app = FastAPI(
    title="FastAPI REST API",
    version="1.0.0",
)


# ============================================================
# CORS - Allow Angular frontend
# ============================================================

cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:4200",
)

allow_origins = [
    origin.strip()
    for origin in cors_origins.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
