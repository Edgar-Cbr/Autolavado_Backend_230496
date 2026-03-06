from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import auth

import crud.crud_categoria_inventario as crud_cat
import schemas.schema_categoria_inventario as schema_cat
import config.db as db_config
import models.model_categoria_inventario as model_cat

categoria = APIRouter()

# crear la tabla si no existe
model_cat.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@categoria.get("/categorias-inventario/", response_model=List[schema_cat.CategoriaInventario], tags=["CategoriasInventario"])
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_cat.get_categorias(db=db, skip=skip, limit=limit)


@categoria.get("/categorias-inventario/{id}", response_model=schema_cat.CategoriaInventario, tags=["CategoriasInventario"])
def read_categoria(id: int, db: Session = Depends(get_db)):
    db_obj = crud_cat.get_categoria(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return db_obj


@categoria.post("/categorias-inventario/", response_model=schema_cat.CategoriaInventario, tags=["CategoriasInventario"])
def create_categoria(categoria_in: schema_cat.CategoriaInventarioCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    return crud_cat.create_categoria(db=db, categoria=categoria_in)


@categoria.put("/categorias-inventario/{id}", response_model=schema_cat.CategoriaInventario, tags=["CategoriasInventario"])
def update_categoria(id: int, categoria_in: schema_cat.CategoriaInventarioUpdate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_cat.update_categoria(db=db, id=id, categoria=categoria_in)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return db_obj


@categoria.delete("/categorias-inventario/{id}", response_model=schema_cat.CategoriaInventario, tags=["CategoriasInventario"])
def delete_categoria(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_cat.delete_categoria(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return db_obj
