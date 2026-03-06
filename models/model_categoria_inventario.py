from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config.db import Base
from datetime import datetime

class CategoriaInventario(Base):
    __tablename__ = "tbc_categorias_inventario"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=True)
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.now)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
