from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_user as crud_user
import config.db as db_config
import schemas.schema_user as schema_user
import models.user as model_user

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema_user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los usuarios"""
    users = crud_user.get_user(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schema_user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Obtener un usuario específico por ID"""
    user = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=schema_user.User)
def create_user(user: schema_user.UserCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    db_user = model_user.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/{user_id}", response_model=schema_user.User)
def update_user(user_id: int, user: schema_user.UserUpdate, db: Session = Depends(get_db)):
    """Actualizar un usuario existente"""
    db_user = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario"""
    db_user = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(db_user)
    db.commit()
    return {"mensaje": "Usuario eliminado exitosamente"}
