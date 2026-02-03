'''Esta clase permite generear el  modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, Datetime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class user(Base):
    '''Modelo para la tabla de usuarios'''
    __tablename__ = "tbb_usuarios"
    id = Column(Integer, primary_key=True, index=True)
    Rol_id = Column(Integer, ForeignKey("tbc_roles.id"))
    