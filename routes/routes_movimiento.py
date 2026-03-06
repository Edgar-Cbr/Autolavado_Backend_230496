from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import auth

import crud.crud_movimiento as crud_mov
import schemas.schema_movimiento as schema_mov
import config.db as db_config
import models.model_movimiento as model_mov

movimiento = APIRouter()

model_mov.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@movimiento.get("/movimientos-inventario/", response_model=List[schema_mov.MovimientoInventario], tags=["MovimientosInventario"])
def read_movimientos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_mov.get_movimientos(db=db, skip=skip, limit=limit)


@movimiento.get("/movimientos-inventario/{id}", response_model=schema_mov.MovimientoInventario, tags=["MovimientosInventario"])
def read_movimiento(id: int, db: Session = Depends(get_db)):
    db_obj = crud_mov.get_movimiento(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_obj


@movimiento.post("/movimientos-inventario/", response_model=schema_mov.MovimientoInventario, tags=["MovimientosInventario"])
def create_movimiento(movimiento_in: schema_mov.MovimientoInventarioCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    return crud_mov.create_movimiento(db=db, movimiento=movimiento_in)


@movimiento.put("/movimientos-inventario/{id}", response_model=schema_mov.MovimientoInventario, tags=["MovimientosInventario"])
def update_movimiento(id: int, movimiento_in: schema_mov.MovimientoInventarioUpdate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_mov.update_movimiento(db=db, id=id, movimiento=movimiento_in)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_obj


@movimiento.delete("/movimientos-inventario/{id}", response_model=schema_mov.MovimientoInventario, tags=["MovimientosInventario"])
def delete_movimiento(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_obj = crud_mov.delete_movimiento(db=db, id=id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_obj
