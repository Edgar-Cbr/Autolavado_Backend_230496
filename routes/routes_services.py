from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_services as crud_services
import config.db as db_config
import schemas.schema_services as schema_services
import models.services as model_services

router = APIRouter(
    prefix="/servicios",
    tags=["servicios"]
)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema_services.Services])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los servicios"""
    services = crud_services.get_services(db, skip=skip, limit=limit)
    return services

@router.get("/{service_id}", response_model=schema_services.Services)
def read_service(service_id: int, db: Session = Depends(get_db)):
    """Obtener un servicio específico por ID"""
    service = db.query(model_services.Services).filter(model_services.Services.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return service

@router.post("/", response_model=schema_services.Services)
def create_service(service: schema_services.ServicesCreate, db: Session = Depends(get_db)):
    """Crear un nuevo servicio"""
    db_service = model_services.Services(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

@router.put("/{service_id}", response_model=schema_services.Services)
def update_service(service_id: int, service: schema_services.ServicesUpdate, db: Session = Depends(get_db)):
    """Actualizar un servicio existente"""
    db_service = db.query(model_services.Services).filter(model_services.Services.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    for key, value in service.dict().items():
        setattr(db_service, key, value)
    
    db.commit()
    db.refresh(db_service)
    return db_service

@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    """Eliminar un servicio"""
    db_service = db.query(model_services.Services).filter(model_services.Services.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    db.delete(db_service)
    db.commit()
    return {"mensaje": "Servicio eliminado exitosamente"}
