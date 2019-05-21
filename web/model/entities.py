from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Usuario(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    codigo = Column(Integer)
    nombre = Column(String(20))
    apellido = Column(String(20))
    password = Column(String(20))
