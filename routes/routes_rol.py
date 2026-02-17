from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_rol as crud_rol
import config.db as db_config
import schemas.schema_rol as schema_rol
import models.rol as model_rol

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema_rol.Rol])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los roles"""
    roles = crud_rol.get_rol(db, skip=skip, limit=limit)
    return roles

@router.get("/{rol_id}", response_model=schema_rol.Rol)
def read_rol(rol_id: int, db: Session = Depends(get_db)):
    """Obtener un rol específico por nombre"""
    rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.post("/", response_model=schema_rol.Rol)
def create_rol(rol: schema_rol.RolCreate, db: Session = Depends(get_db)):
    """Crear un nuevo rol"""
    db_rol = model_rol.Rol(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

@router.put("/{rol_id}", response_model=schema_rol.Rol)
def update_rol(rol_id: int, rol: schema_rol.RolUpdate, db: Session = Depends(get_db)):
    """Actualizar un rol existente"""
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    for key, value in rol.dict().items():
        setattr(db_rol, key, value)
    
    db.commit()
    db.refresh(db_rol)
    return db_rol

@router.delete("/{rol_id}")
def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    """Eliminar un rol"""
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    db.delete(db_rol)
    db.commit()
    return {"mensaje": "Rol eliminado exitosamente"}