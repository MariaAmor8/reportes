from fastapi import HTTPException
from models.db import reportes_collection  # Importa el modelo Reporte
from fastapi.encoders import jsonable_encoder  # Para convertir el resultado en JSON
from models.models import Reporte, ReporteCollection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

async def get_reportes():
    """
    Get a list of reportes
    :return: A list of reportes
    """
    reportes = await reportes_collection.find().to_list(1000)
    return ReporteCollection(reportes=reportes)
    
async def get_reporte(reporte_code: str):
    """
    Get a single reporte
    :param reporte_code: The code of the reporte
    :return: The reporte
    """
    if (reporte := await reportes_collection.find_one({"code": reporte_code})) is not None:
        return reporte

    raise HTTPException(
        status_code=404, detail=f"reporte with code {reporte_code} not found"
    )
    
async def create_reporte(reporte: Reporte):
    """
    Insert a new reporte record.
    """
    try:
        new_reporte = await reportes_collection.insert_one(
            reporte.model_dump(by_alias=True, exclude=["id"])
        )
        created_reporte = await reportes_collection.find_one({"_id": new_reporte.inserted_id})
        return created_reporte

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"reporte with code {reporte.code} already exists"
        )
        
async def delete_reporte(reporte_code: str):
    """
    Delete a reporte
    :param reporte_code: The code of the reporte
    """
    delete_result = await reportes_collection.delete_one({"code": reporte_code})

    if delete_result.deleted_count == 1:
        return

    raise HTTPException(
        status_code=404, detail=f"Reporte with code {reporte_code} not found"
    )