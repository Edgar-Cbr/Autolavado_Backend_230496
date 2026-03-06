from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class MovimientoInventarioBase(BaseModel):
    producto_Id: int
    tipo_movimiento: str
    cantidad: int
    fecha_movimiento: Optional[datetime] = None
    usuario_Id: int

class MovimientoInventarioCreate(MovimientoInventarioBase):
    pass

class MovimientoInventarioUpdate(MovimientoInventarioBase):
    producto_Id: Optional[int] = None
    tipo_movimiento: Optional[str] = None
    cantidad: Optional[int] = None
    fecha_movimiento: Optional[datetime] = None
    usuario_Id: Optional[int] = None

class MovimientoInventario(MovimientoInventarioBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)
