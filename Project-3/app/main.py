from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes import router

# Create Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudyHub API")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "StudyHub API is Running"}