from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_auto as crud_auto
import config.db as db_config
import schemas.schema_auto as schema_auto
import models.auto as model_auto

router = APIRouter(
    prefix="/autos",
    tags=["autos"]
)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema_auto.Auto])
def read_autos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los autos"""
    autos = crud_auto.get_auto(db, skip=skip, limit=limit)
    return autos

@router.get("/{auto_id}", response_model=schema_auto.Auto)
def read_auto(auto_id: int, db: Session = Depends(get_db)):
    """Obtener un auto específico por ID"""
    auto = db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto

@router.post("/", response_model=schema_auto.Auto)
def create_auto(auto: schema_auto.AutoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo auto"""
    db_auto = model_auto.Auto(**auto.dict())
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto

@router.put("/{auto_id}", response_model=schema_auto.Auto)
def update_auto(auto_id: int, auto: schema_auto.AutoUpdate, db: Session = Depends(get_db)):
    """Actualizar un auto existente"""
    db_auto = db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()
    if not db_auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    
    for key, value in auto.dict().items():
        setattr(db_auto, key, value)
    
    db.commit()
    db.refresh(db_auto)
    return db_auto

@router.delete("/{auto_id}")
def delete_auto(auto_id: int, db: Session = Depends(get_db)):
    """Eliminar un auto"""
    db_auto = db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()
    if not db_auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    
    db.delete(db_auto)
    db.commit()
    return {"mensaje": "Auto eliminado exitosamente"}
