from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from logic.reportes_logic import obtener_reportes, obtener_reporte_por_id, crear_reporte, borrar_reporte
from models.db import SessionLocal
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/reportes/", response_model=list)  # Define la ruta para obtener todos los reportes
async def get_all_reportes(db: Session = Depends(get_db)):
    try:
        # Llama a la función para obtener los reportes
        reportes = obtener_reportes(db)
        return reportes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get("/reportes/{reporte_id}/", response_model=dict)  # Ruta para obtener el reporte por ID
async def get_reporte(reporte_id: int, db: Session = Depends(get_db)):
    # Llama a la función para obtener el reporte por ID
    reporte = obtener_reporte_por_id(db, reporte_id)
    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return reporte

class ReporteCreate(BaseModel):
    fechaEmision: str
    emisor: str
    estudiante: int

@router.post("/reportes/", response_model=dict)  # Ruta para crear un reporte
async def crear_reporte_api(reporte: ReporteCreate, db: Session = Depends(get_db)):
    try:
        # Llama a la función para crear un reporte
        nuevo_reporte = crear_reporte(db, reporte.fechaEmision, reporte.emisor, reporte.estudiante)
        return {"id": nuevo_reporte.id, "fechaEmision": nuevo_reporte.fechaEmision, "emisor": nuevo_reporte.emisor, "estudiante": nuevo_reporte.estudiante}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.delete("/reportes/{reporte_id}/", response_model=dict)  # Ruta para borrar un reporte
async def delete_reporte(reporte_id: int, db: Session = Depends(get_db)):
    # Llama a la función para borrar el reporte por ID
    reporte = borrar_reporte(db, reporte_id)
    
    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    
    return {"message": "Reporte eliminado", "id": reporte.id}