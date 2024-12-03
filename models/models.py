
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId
    
class Reporte(BaseModel):
    code: str = Field(...)
    fechaEmision: str = Field(...)
    emisor: str = Field(...)
    estudiante: int = Field(...)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "code": "1",
                "fechaEmision": "2024-01-01",
                "emisor": "Juanito Perez",
                "estudiante": 1234,
            }
        },
    )

class ReporteOut(Reporte):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "code": "1",
                "fechaEmision": "2024-01-01",
                "emisor": "Juanito Perez",
                "estudiante": 1234,
            }
        },
    )
    
class ReporteCollection(BaseModel):
    # A collection of reportes
    reportes: List[ReporteOut] = Field(...)