from fastapi import APIRouter, status, Body
import logic.reportes_logic as reportes_service
from models.models import Reporte, ReporteOut, ReporteCollection


router = APIRouter()
ENDPOINT_NAME = "/reportes"

@router.get(
    "/",
    response_description="List all rportes",
    response_model=ReporteCollection,
    status_code=status.HTTP_200_OK,
)
async def get_reportes():
    return await reportes_service.get_reportes()


@router.post(
    "/",
    response_description="Create a new reporte",
    response_model=ReporteOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_reporte(reporte: Reporte = Body(...)):
    return await reportes_service.create_reporte(reporte)


@router.delete(
    "/{reporte_code}",
    response_description="Delete a reporte",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_reporte(reporte_code: str):
    return await reportes_service.delete_reporte(reporte_code)