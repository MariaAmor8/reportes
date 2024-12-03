from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
import models.db
import models.models
from models.db import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from views.reportes_views import router as reportes_router

app = FastAPI()
models.models.Base.metadata.create_all(bind=engine)
app.include_router(reportes_router)

class ReporteBase(BaseModel):
    fechaEmision: str
    emisor: str
    estudiante: int #el id del estudiante o el numId

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        