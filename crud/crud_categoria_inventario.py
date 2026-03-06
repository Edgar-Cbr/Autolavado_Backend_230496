from sqlalchemy.orm import Session
import models.model_categoria_inventario as model_cat
import schemas.schema_categoria_inventario as schema_cat


def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_cat.CategoriaInventario).offset(skip).limit(limit).all()


def get_categoria(db: Session, id: int):
    return db.query(model_cat.CategoriaInventario).filter(model_cat.CategoriaInventario.Id == id).first()


def create_categoria(db: Session, categoria: schema_cat.CategoriaInventarioCreate):
    db_obj = model_cat.CategoriaInventario(
        nombre=categoria.nombre,
        descripcion=categoria.descripcion,
        estado=categoria.estado,
        fecha_registro=categoria.fecha_registro,
        fecha_actualizacion=categoria.fecha_actualizacion,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_categoria(db: Session, id: int, categoria: schema_cat.CategoriaInventarioUpdate):
    db_obj = db.query(model_cat.CategoriaInventario).filter(model_cat.CategoriaInventario.Id == id).first()
    if db_obj:
        update_data = categoria.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_categoria(db: Session, id: int):
    db_obj = db.query(model_cat.CategoriaInventario).filter(model_cat.CategoriaInventario.Id == id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
