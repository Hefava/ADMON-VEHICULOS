from sqlalchemy import Column, Date, DateTime, CHAR, DECIMAL, INT, TEXT
from config.dbconnection import Base

class CajaRecaudos(Base):
    __tablename__ = 'CAJARECAUDOS'

    RECIBO = Column(CHAR(8), primary_key=True)
    FEC_RECIBO = Column(Date)
    HOR_RECIBO = Column(CHAR(8))
    PLACA = Column(CHAR(8))
    NUMERO = Column(CHAR(8))
    KILO_ANTES = Column(DECIMAL(8, 0))
    KILOM_DIA = Column(DECIMAL(8, 0))
    KILOMETRAJ = Column(DECIMAL(8, 0))
    CLIENTE = Column(CHAR(12))
    CONDUCTOR = Column(CHAR(12))
    CEDULA = Column(CHAR(12))
    NIT = Column(CHAR(12))
    PROPI_IDEN = Column(CHAR(12))
    CTA_GASTO = Column(CHAR(10))
    ZONA = Column(CHAR(2))
    CLASIFICAC = Column(CHAR(1))
    FORMAPAGO = Column(CHAR(2))
    NOMFORMAPA = Column(CHAR(20))
    BANCO = Column(CHAR(2))
    BANCO_CTA = Column(CHAR(15))
    CHEQUE_NRO = Column(CHAR(8))
    CHEQUE_FEC = Column(Date)
    CHEQUE_VLR = Column(DECIMAL(12, 2))
    TOTAL = Column(DECIMAL(12, 2))
    NROENTREGA = Column(DECIMAL(12, 2))
    NROENTPAGO = Column(DECIMAL(12, 2))
    NROENTSDO = Column(DECIMAL(12, 2))
    PAGAS = Column(DECIMAL(12, 2))
    VLR_PERSON = Column(DECIMAL(12, 2))
    VLR_RC = Column(DECIMAL(12, 2))
    VLR_ND = Column(DECIMAL(12, 2))
    VLR_NC = Column(DECIMAL(12, 2))
    VLR_INTER = Column(DECIMAL(12, 2))
    SDO_PERSON = Column(DECIMAL(12, 2))
    SDO_RC = Column(DECIMAL(12, 2))
    SDO_ND = Column(DECIMAL(12, 2))
    SDO_NC = Column(DECIMAL(12, 2))
    SDO_INTER = Column(DECIMAL(12, 2))
    VLR_CUOTA = Column(DECIMAL(12, 2))
    RESTANTE = Column(DECIMAL(12, 2))
    DESCUENTOS = Column(DECIMAL(12, 2))
    RTE_FTE = Column(DECIMAL(12, 2))
    RTE_ICA = Column(DECIMAL(12, 2))
    RTE_IVA = Column(DECIMAL(12, 2))
    TIPO = Column(CHAR(2))
    FACTURA = Column(CHAR(12))
    FEC_FACTU = Column(CHAR(8))
    CRUCE_ANTI = Column(CHAR(1))
    FON_INSCRI = Column(DECIMAL(12, 2))
    FON_FERIAD = Column(DECIMAL(12, 2))
    FON_AHORRO = Column(DECIMAL(12, 2))
    FON_MANTEN = Column(DECIMAL(12, 2))
    FON_OTROS = Column(DECIMAL(12, 2))
    DEU_ANTICI = Column(DECIMAL(12, 2))
    DEU_RENTA = Column(DECIMAL(12, 2))
    DEU_SINIES = Column(DECIMAL(12, 2))
    DEU_OTRAS = Column(DECIMAL(12, 2))
    SDO_INSCRI = Column(DECIMAL(12, 2))
    SDO_FERIAD = Column(DECIMAL(12, 2))
    SDO_AHORRO = Column(DECIMAL(12, 2))
    SDO_MANTEN = Column(DECIMAL(12, 2))
    SDO_OTROS = Column(DECIMAL(12, 2))
    SDO_ANTICI = Column(DECIMAL(12, 2))
    SDO_RENTA = Column(DECIMAL(12, 2))
    SDO_SINIES = Column(DECIMAL(12, 2))
    SDO_OTRAS = Column(DECIMAL(12, 2))
    SALDO_ANT = Column(DECIMAL(12, 2))
    FACTURACIO = Column(DECIMAL(12, 2))
    PAGO_EFECT = Column(DECIMAL(12, 2))
    PAGO_DEPOS = Column(DECIMAL(12, 2))
    TRANSFEREN = Column(DECIMAL(12, 2))
    NOTA_DEB = Column(DECIMAL(12, 2))
    NOTA_CRE = Column(DECIMAL(12, 2))
    SALDO_ACT = Column(DECIMAL(12, 2))
    DETALLE = Column(TEXT)
    LLAMADAS = Column(TEXT)
    INTERNO = Column(TEXT)
    FEC_IMPRES = Column(Date)
    HOR_IMPRES = Column(CHAR(8))
    BOLSA = Column(CHAR(1))
    BOLSA_NRO = Column(INT)
    BOLSA_FEC = Column(Date)
    TRASLADA = Column(CHAR(1))
    FEC_TRASLA = Column(DateTime)
    USUARIO = Column(CHAR(10))
    USU_ANULA = Column(CHAR(10))
    FEC_ANULA = Column(Date)
    FEC_DOCUM = Column(CHAR(8))
    FEC_CREADO = Column(DateTime)
    WRECIBO = Column(CHAR(8))
    EX = Column(CHAR(1))
    MARCA = Column(CHAR(1))