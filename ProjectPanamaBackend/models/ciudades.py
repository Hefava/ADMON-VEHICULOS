from sqlalchemy import Column, DateTime, CHAR
from config.dbconnection import Base

class Ciudades(Base):
  __tablename__ = 'CIUDADES'

  CODIGO = Column(CHAR(5), primary_key=True)
  NOMBRE = Column(CHAR(40))
  DEPTO = Column(CHAR(25))
  FEC_CREADO = Column(DateTime)