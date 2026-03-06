from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.db import Base
from datetime import datetime

class MovimientoInventario(Base):
    __tablename__ = "tbd_movimientos_inventario"

    Id = Column(Integer, primary_key=True, index=True)
    producto_Id = Column(Integer, ForeignKey("tbc_productos.Id"), nullable=False)
    tipo_movimiento = Column(String(20))  # "Entrada" o "Salida"
    cantidad = Column(Integer, nullable=False)
    fecha_movimiento = Column(DateTime, default=datetime.now)
    usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
