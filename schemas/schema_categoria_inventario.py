from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class CategoriaInventarioBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    estado: bool = True
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class CategoriaInventarioCreate(CategoriaInventarioBase):
    pass

class CategoriaInventarioUpdate(CategoriaInventarioBase):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[bool] = None

class CategoriaInventario(CategoriaInventarioBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)
