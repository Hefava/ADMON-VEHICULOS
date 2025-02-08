from sqlalchemy import Column, Date, DateTime, CHAR, DECIMAL, TEXT
from config.dbconnection import Base

class Movimien(Base):
  __tablename__ = 'MOVIMIEN'

  ORIGEN = Column(CHAR(3))
  CODIGO = Column(CHAR(18), primary_key=True)
  PEDIDA = Column(DECIMAL(10, 2))
  CANTIDAD = Column(DECIMAL(10, 2))
  VALOR = Column(DECIMAL(12, 2))
  GASTO = Column(DECIMAL(12, 2))
  DCTO_ARTC = Column(DECIMAL(5, 2))
  DCTO_VALOR = Column(DECIMAL(12, 2))
  IVA_ARTIC = Column(DECIMAL(2, 0))
  IVA_VALOR = Column(DECIMAL(12, 2))
  VALOR1 = Column(DECIMAL(12, 2))
  PAGO_PROPI = Column(DECIMAL(3, 0))
  PAGO_CONDU = Column(DECIMAL(3, 0))
  TOTA_PROPI = Column(DECIMAL(12, 2))
  TOTA_CONDU = Column(DECIMAL(12, 2))
  TOTAL = Column(DECIMAL(12, 2))
  TOTAL7 = Column(DECIMAL(12, 2))
  NOMBRE = Column(CHAR(60))
  PRESENTA = Column(CHAR(30))
  COSTO = Column(DECIMAL(12, 2))
  SALDO = Column(DECIMAL(12, 2))
  VLR_TOT = Column(DECIMAL(12, 2))
  CTO_TOT = Column(DECIMAL(12, 2))
  TIPO = Column(CHAR(3))
  TIPNOM = Column(CHAR(4))
  FACTURA = Column(CHAR(8))
  FORMAPAGO = Column(CHAR(2))
  COMBO = Column(CHAR(10))
  CON_CLI = Column(DECIMAL(1, 0))
  FECHA = Column(Date)
  PLACA = Column(CHAR(8))
  UNIDAD = Column(CHAR(8))
  KILOMETRAJ = Column(DECIMAL(8, 0))
  FEC_DOCUM = Column(CHAR(8))
  HOR_DOCUM = Column(CHAR(8))
  ANO = Column(CHAR(4))
  MES = Column(CHAR(2))
  DIA = Column(CHAR(2))
  PROVEDOR = Column(CHAR(12))
  CLIENTE = Column(CHAR(12))
  CONDUCTOR = Column(CHAR(20))
  IDENTIFICA = Column(CHAR(20))
  ESTADO = Column(CHAR(1))
  FEC_ESTADO = Column(Date)
  LOTE = Column(CHAR(20))
  FEC_VENCE = Column(Date)
  INVIMA = Column(CHAR(20))
  DOSIS = Column(CHAR(60))
  BODEGA = Column(CHAR(3))
  DESTINO = Column(CHAR(3))
  VENDEDOR = Column(CHAR(12))
  MECANICO = Column(CHAR(12))
  PROPI_IDEN = Column(CHAR(12))
  ZONA = Column(CHAR(2))
  REGISTRO = Column(CHAR(8))
  PEDIDO = Column(CHAR(8))
  FEC_PEDIDO = Column(Date)
  GRUPO = Column(CHAR(4))
  FAC_VTA = Column(CHAR(8))
  FEC_FACVTA = Column(Date)
  MARCA = Column(CHAR(1))
  CODIBARR = Column(CHAR(18))
  CAJERO = Column(CHAR(10))
  USUARIO = Column(CHAR(10))
  FEC_CREACI = Column(CHAR(10))
  USU_MODIFI = Column(CHAR(10))
  FEC_MODIFI = Column(CHAR(10))
  TRASLADA = Column(CHAR(1))
  FEC_TRASLA = Column(Date)