from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from config.db import Base
from datetime import datetime

class Producto(Base):
    __tablename__ = "tbc_productos"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(300), nullable=True)
    categoria_Id = Column(Integer, ForeignKey("tbc_categorias_inventario.Id"))
    unidad_medida = Column(String(50))
    stock_actual = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    precio_compra = Column(Float, default=0.0)
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.now)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
