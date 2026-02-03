'''Esta clase permite generear el  modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, Datetime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    '''Modelo para la tabla de roles'''
    __tablename__ = "tbc_roles"
    id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(15))
    estado = Column(Boolean)