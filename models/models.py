
from sqlalchemy import Column, Integer, String
from models.db import Base
    
class Reporte(Base):
    __tablename__ = 'reportes'
    id = Column(Integer, primary_key=True, index=True)
    fechaEmision = Column(String)
    emisor = Column(String)
    estudiante = Column(Integer)
