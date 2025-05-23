from sqlalchemy import Column, Date, DateTime, CHAR, DECIMAL, TEXT
from config.dbconnection import Base

class Cartera(Base):
    __tablename__ = 'CARTERA'

    FACTURA = Column(CHAR(12), primary_key=True)
    EMPRESA = Column(CHAR(2))
    TIPO = Column(CHAR(2))
    NOMTIPO = Column(CHAR(10))
    PLAZO = Column(DECIMAL(4, 0))
    CLIENTE = Column(CHAR(12))
    CEDULA = Column(CHAR(12))
    CLASIFICAC = Column(CHAR(1))
    ZONA = Column(CHAR(2))
    VENDEDOR = Column(CHAR(12))
    CIUDAD = Column(CHAR(5))
    PLACA = Column(CHAR(12))
    UNIDAD = Column(CHAR(5))
    PROPI_IDEN = Column(CHAR(12))
    FEC_ENTREG = Column(Date)
    MORA = Column(DECIMAL(4, 0))
    VALOR = Column(DECIMAL(12, 2))
    FECHA = Column(Date)
    FEC_FACTU = Column(Date)
    DOC_FACTU = Column(CHAR(12))
    CAN_FACTU = Column(DECIMAL(4, 0))
    ABONOS = Column(DECIMAL(12, 2))
    FEC_ABONO = Column(Date)
    DOC_ABONO = Column(CHAR(12))
    CAN_ABONO = Column(DECIMAL(4, 0))
    INTERESES = Column(DECIMAL(12, 2))
    FEC_INTER = Column(Date)
    DOC_INTER = Column(CHAR(12))
    CAN_INTER = Column(DECIMAL(4, 0))
    DESCUENTOS = Column(DECIMAL(12, 2))
    FEC_DESCU = Column(Date)
    DOC_DESCU = Column(CHAR(12))
    CAN_DESCU = Column(DECIMAL(4, 0))
    N_DEB = Column(DECIMAL(12, 2))
    FEC_NDEB = Column(Date)
    DOC_NDEB = Column(CHAR(12))
    CAN_NDEB = Column(DECIMAL(4, 0))
    N_CRE = Column(DECIMAL(12, 2))
    FEC_NCRE = Column(Date)
    DOC_NCRE = Column(CHAR(12))
    CAN_NCRE = Column(DECIMAL(4, 0))
    DETALLE = Column(TEXT)
    DOC_CRUCE = Column(CHAR(8))
    VLR_CRUCE = Column(DECIMAL(12, 2))
    FEC_CRUCE = Column(Date)
    FEC_DESDE = Column(Date)
    FEC_HASTA = Column(Date)
    FACTRELA = Column(CHAR(10))
    CRUCE = Column(DECIMAL(1, 0))
    SALDO = Column(DECIMAL(12, 2))
    FEC_CUADRE = Column(Date)
    FEC_DOC = Column(CHAR(8))
    SALDO00 = Column(DECIMAL(12, 2))
    DEB01 = Column(DECIMAL(12, 2))
    CRE01 = Column(DECIMAL(12, 2))
    SALDO01 = Column(DECIMAL(12, 2))
    DEB02 = Column(DECIMAL(12, 2))
    CRE02 = Column(DECIMAL(12, 2))
    SALDO02 = Column(DECIMAL(12, 2))
    DEB03 = Column(DECIMAL(12, 2))
    CRE03 = Column(DECIMAL(12, 2))
    SALDO03 = Column(DECIMAL(12, 2))
    DEB04 = Column(DECIMAL(12, 2))
    CRE04 = Column(DECIMAL(12, 2))
    SALDO04 = Column(DECIMAL(12, 2))
    DEB05 = Column(DECIMAL(12, 2))
    CRE05 = Column(DECIMAL(12, 2))
    SALDO05 = Column(DECIMAL(12, 2))
    DEB06 = Column(DECIMAL(12, 2))
    CRE06 = Column(DECIMAL(12, 2))
    SALDO06 = Column(DECIMAL(12, 2))
    DEB07 = Column(DECIMAL(12, 2))
    CRE07 = Column(DECIMAL(12, 2))
    SALDO07 = Column(DECIMAL(12, 2))
    DEB08 = Column(DECIMAL(12, 2))
    CRE08 = Column(DECIMAL(12, 2))
    SALDO08 = Column(DECIMAL(12, 2))
    DEB09 = Column(DECIMAL(12, 2))
    CRE09 = Column(DECIMAL(12, 2))
    SALDO09 = Column(DECIMAL(12, 2))
    DEB10 = Column(DECIMAL(12, 2))
    CRE10 = Column(DECIMAL(12, 2))
    SALDO10 = Column(DECIMAL(12, 2))
    DEB11 = Column(DECIMAL(12, 2))
    CRE11 = Column(DECIMAL(12, 2))
    SALDO11 = Column(DECIMAL(12, 2))
    DEB12 = Column(DECIMAL(12, 2))
    CRE12 = Column(DECIMAL(12, 2))
    SALDO12 = Column(DECIMAL(12, 2))
    FEC_DOCUM = Column(CHAR(8))
    FEC_CREADO = Column(Date)
    USU_CREADO = Column(CHAR(8))
    FEC_MODIFI = Column(Date)
    USU_MODIFI = Column(CHAR(8))
    FEC_HABILI = Column(Date)
    USU_HABILI = Column(CHAR(8))
    PROCESO = Column(CHAR(1))
    EX = Column(CHAR(1))
    SEL = Column(CHAR(1))
    PAGO = Column(DECIMAL(1, 0))
