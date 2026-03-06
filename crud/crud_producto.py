from sqlalchemy.orm import Session
import models.model_producto as model_prod
import schemas.schema_producto as schema_prod


def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_prod.Producto).offset(skip).limit(limit).all()


def get_producto(db: Session, id: int):
    return db.query(model_prod.Producto).filter(model_prod.Producto.Id == id).first()


def create_producto(db: Session, producto: schema_prod.ProductoCreate):
    db_obj = model_prod.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        categoria_Id=producto.categoria_Id,
        unidad_medida=producto.unidad_medida,
        stock_actual=producto.stock_actual,
        stock_minimo=producto.stock_minimo,
        precio_compra=producto.precio_compra,
        estado=producto.estado,
        fecha_registro=producto.fecha_registro,
        fecha_actualizacion=producto.fecha_actualizacion,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_producto(db: Session, id: int, producto: schema_prod.ProductoUpdate):
    db_obj = db.query(model_prod.Producto).filter(model_prod.Producto.Id == id).first()
    if db_obj:
        update_data = producto.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_producto(db: Session, id: int):
    db_obj = db.query(model_prod.Producto).filter(model_prod.Producto.Id == id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
