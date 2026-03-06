from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import auth

import crud.crud_producto as crud_prod
import schemas.schema_producto as schema_prod
import config.db as db_config
import models.model_producto as model_prod

producto = APIRouter()

model_prod.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@producto.get("/productos/", response_model=List[schema_prod.Producto], tags=["Productos"])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_prod.get_productos(db=db, skip=skip, limit=limit)


@producto.get("/productos/{id}", response_model=schema_prod.Producto, tags=["Productos"])
def read_producto(id: int, db: Session = Depends(get_db)):
    db_obj = crud_prod.get_producto(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_obj


@producto.post("/productos/", response_model=schema_prod.Producto, tags=["Productos"])
def create_producto(producto_in: schema_prod.ProductoCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    return crud_prod.create_producto(db=db, producto=producto_in)


@producto.put("/productos/{id}", response_model=schema_prod.Producto, tags=["Productos"])
def update_producto(id: int, producto_in: schema_prod.ProductoUpdate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_prod.update_producto(db=db, id=id, producto=producto_in)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_obj


@producto.delete("/productos/{id}", response_model=schema_prod.Producto, tags=["Productos"])
def delete_producto(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_prod.delete_producto(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_obj
