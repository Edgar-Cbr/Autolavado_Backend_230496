from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria_Id: int
    unidad_medida: str
    stock_actual: int = 0
    stock_minimo: int = 0
    precio_compra: float = 0.0
    estado: bool = True
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    categoria_Id: Optional[int] = None
    unidad_medida: Optional[str] = None
    stock_actual: Optional[int] = None
    stock_minimo: Optional[int] = None
    precio_compra: Optional[float] = None
    estado: Optional[bool] = None

class Producto(ProductoBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)
