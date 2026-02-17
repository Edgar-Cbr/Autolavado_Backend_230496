from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_auto_servicio as crud_auto_servicio
import config.db as db_config
import schemas.schema_auto_servicio as schema_auto_servicio
import models.auto_servicio as model_auto_servicio

router = APIRouter(
    prefix="/auto-servicios",
    tags=["auto-servicios"]
)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema_auto_servicio.AutoServicio])
def read_auto_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los autos con servicios"""
    auto_servicios = crud_auto_servicio.get_auto_servicio(db, skip=skip, limit=limit)
    return auto_servicios

@router.get("/{auto_servicio_id}", response_model=schema_auto_servicio.AutoServicio)
def read_auto_servicio(auto_servicio_id: int, db: Session = Depends(get_db)):
    """Obtener un auto-servicio específico por ID"""
    auto_servicio = db.query(model_auto_servicio.AutoServicio).filter(model_auto_servicio.AutoServicio.id == auto_servicio_id).first()
    if not auto_servicio:
        raise HTTPException(status_code=404, detail="Auto-servicio no encontrado")
    return auto_servicio

@router.post("/", response_model=schema_auto_servicio.AutoServicio)
def create_auto_servicio(auto_servicio: schema_auto_servicio.AutoServicioCreate, db: Session = Depends(get_db)):
    """Crear una nueva relación auto-servicio"""
    db_auto_servicio = model_auto_servicio.AutoServicio(**auto_servicio.dict())
    db.add(db_auto_servicio)
    db.commit()
    db.refresh(db_auto_servicio)
    return db_auto_servicio

@router.put("/{auto_servicio_id}", response_model=schema_auto_servicio.AutoServicio)
def update_auto_servicio(auto_servicio_id: int, auto_servicio: schema_auto_servicio.AutoServicioUpdate, db: Session = Depends(get_db)):
    """Actualizar una relación auto-servicio existente"""
    db_auto_servicio = db.query(model_auto_servicio.AutoServicio).filter(model_auto_servicio.AutoServicio.id == auto_servicio_id).first()
    if not db_auto_servicio:
        raise HTTPException(status_code=404, detail="Auto-servicio no encontrado")
    
    for key, value in auto_servicio.dict().items():
        setattr(db_auto_servicio, key, value)
    
    db.commit()
    db.refresh(db_auto_servicio)
    return db_auto_servicio

@router.delete("/{auto_servicio_id}")
def delete_auto_servicio(auto_servicio_id: int, db: Session = Depends(get_db)):
    """Eliminar una relación auto-servicio"""
    db_auto_servicio = db.query(model_auto_servicio.AutoServicio).filter(model_auto_servicio.AutoServicio.id == auto_servicio_id).first()
    if not db_auto_servicio:
        raise HTTPException(status_code=404, detail="Auto-servicio no encontrado")
    
    db.delete(db_auto_servicio)
    db.commit()
    return {"mensaje": "Auto-servicio eliminado exitosamente"}
