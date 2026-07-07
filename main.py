from fastapi import FastAPI
import os

app = FastAPI(title="FastAPI + PostgreSQL Module Assignment")


@app.get("/")
def root():
    return {"status": "ok", "database_url_set": bool(os.getenv("DATABASE_URL"))}


@app.get("/health")
def health():
    return {"health": "ok"}
