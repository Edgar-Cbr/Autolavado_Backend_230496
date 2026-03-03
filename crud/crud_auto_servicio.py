from sqlalchemy.orm import Session
from models.model_auto_servicio import VehiculoServicio
import schemas.schema_auto_servicio as schema_auto_servicio


def get_auto_servicios(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener todos los registros de auto_servicio'''
    return db.query(VehiculoServicio).offset(skip).limit(limit).all()


def get_auto_servicio(db: Session, id: int):
    '''Función para obtener un solo registro por ID'''
    return db.query(VehiculoServicio).filter(VehiculoServicio.Id == id).first()


def create_auto_servicio(
    db: Session,
    auto_servicio: schema_auto_servicio.UsuarioVehiculoServicioCreate
):
    '''Función para insertar un nuevo registro'''
    db_auto_servicio = VehiculoServicio(
        vehiculo_Id=auto_servicio.vehiculo_Id,
        cajero_Id=auto_servicio.cajero_Id,
        operativo_Id=auto_servicio.operativo_Id,
        servicio_Id=auto_servicio.servicio_Id,
        fecha=auto_servicio.fecha,
        hora=auto_servicio.hora,
        estatus=auto_servicio.estatus,
        estado=auto_servicio.estado
    )

    db.add(db_auto_servicio)
    db.commit()
    db.refresh(db_auto_servicio)
    return db_auto_servicio


def update_auto_servicio(
    db: Session,
    id: int,
    auto_servicio: schema_auto_servicio.UsuarioVehiculoServicioUpdate
):
    '''Función para actualizar un registro existente'''
    db_obj = get_auto_servicio(db, id)
    if not db_obj:
        return None

    update_data = auto_servicio.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_auto_servicio(db: Session, id: int):
    '''Función para eliminar un registro'''
    db_obj = get_auto_servicio(db, id)
    if not db_obj:
        return None

    db.delete(db_obj)
    db.commit()
    return db_obj