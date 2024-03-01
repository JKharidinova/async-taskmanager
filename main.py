from fastapi import FastAPI
from sqlalchemy.orm import Session

from src.settings import settings
from src.db import SessionLocal, engine

app = FastAPI(title=settings.PROJECT_NAME,)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}
