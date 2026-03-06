from sqlalchemy.orm import Session
import models.model_movimiento as model_mov
import schemas.schema_movimiento as schema_mov


def get_movimientos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_mov.MovimientoInventario).offset(skip).limit(limit).all()


def get_movimiento(db: Session, id: int):
    return db.query(model_mov.MovimientoInventario).filter(model_mov.MovimientoInventario.Id == id).first()


def create_movimiento(db: Session, movimiento: schema_mov.MovimientoInventarioCreate):
    db_obj = model_mov.MovimientoInventario(
        producto_Id=movimiento.producto_Id,
        tipo_movimiento=movimiento.tipo_movimiento,
        cantidad=movimiento.cantidad,
        fecha_movimiento=movimiento.fecha_movimiento,
        usuario_Id=movimiento.usuario_Id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_movimiento(db: Session, id: int, movimiento: schema_mov.MovimientoInventarioUpdate):
    db_obj = db.query(model_mov.MovimientoInventario).filter(model_mov.MovimientoInventario.Id == id).first()
    if db_obj:
        update_data = movimiento.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_movimiento(db: Session, id: int):
    db_obj = db.query(model_mov.MovimientoInventario).filter(model_mov.MovimientoInventario.Id == id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
