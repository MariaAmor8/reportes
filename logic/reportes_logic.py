from fastapi import HTTPException
from sqlalchemy.orm import Session
import models.models  # Importa el modelo Reporte
from fastapi.encoders import jsonable_encoder  # Para convertir el resultado en JSON
from models.models import Reporte

async def get_reportes():
    print("hola")
    
    
def obtener_reportes(db: Session):
    # Obtener todos los reportes de la base de datos
    reportes = db.query(models.models.Reporte).all()
    
    # Convertir los reportes a formato JSON
    return jsonable_encoder(reportes)


def obtener_reporte_por_id(db: Session, reporte_id: int):
    # Obtener el reporte por ID
    reporte = db.query(models.models.Reporte).filter(models.models.Reporte.id == reporte_id).first()
    
    if reporte is None:
        return None  # Si no se encuentra el reporte, retornamos None
    
    return jsonable_encoder(reporte)  # Convertimos el reporte a formato JSON


def crear_reporte(db: Session, fecha_emision: str, emisor: str, estudiante: int):
    # Crear una instancia del reporte con los datos recibidos
    nuevo_reporte = Reporte(fechaEmision=fecha_emision, emisor=emisor, estudiante=estudiante)
    
    # Añadirlo a la sesión
    db.add(nuevo_reporte)
    db.commit()  # Confirmar la transacción
    
    # Refrescar el objeto para obtener el ID generado
    db.refresh(nuevo_reporte)
    
    return nuevo_reporte  # Retorna el nuevo reporte creado


def borrar_reporte(db: Session, reporte_id: int):
    # Buscar el reporte por su ID
    reporte = db.query(Reporte).filter(Reporte.id == reporte_id).first()
    
    if reporte is None:
        return None  # Si no se encuentra el reporte, retornar None
    
    # Si el reporte existe, eliminarlo
    db.delete(reporte)
    db.commit()  # Confirmar la eliminación
    
    return reporte  # Retorna el reporte eliminado
