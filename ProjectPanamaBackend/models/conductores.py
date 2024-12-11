from config.dbconnection import Base
from sqlalchemy import Column, String, Numeric, DateTime, CHAR, DECIMAL, Date, Boolean

class Conductores(Base):
  __tablename__ = "CONDUCTORES"

  CODIGO = Column(CHAR(12), primary_key=True)
  NOMBRE = Column(CHAR(50), default='')
  CEDULA = Column(CHAR(12), default='')
  NIT = Column(CHAR(12), default='')
  CONTROL = Column(DECIMAL(2,0), default=0)
  CIUDAD = Column(CHAR(5), default='')
  NOMCIUDAD = Column(CHAR(40), default='')
  DIRECCION = Column(CHAR(120), default='')
  TELEFONO = Column(CHAR(30), default='')
  CELULAR = Column(CHAR(30), default='')
  REPRESENTA = Column(CHAR(30), default='')
  CONTACTO = Column(CHAR(40), default='')
  TEL_CONTAC = Column(CHAR(40), default='')
  PAR_CONTAC = Column(CHAR(20), default='')
  CONTACTO1 = Column(CHAR(20), default='')
  TEL_CONTA1 = Column(CHAR(40), default='')
  PAR_CONTA1 = Column(CHAR(20), default='')
  CONTACTO2 = Column(CHAR(20), default='')
  TEL_CONTA2 = Column(CHAR(40), default='')
  PAR_CONTA2 = Column(CHAR(20), default='')
  CORREO = Column(CHAR(40), default='')
  FEC_NACIMT = Column(Date, default=None)
  SEXO = Column(CHAR(1), default="")
  ESTA_CIVIL = Column(CHAR(1), default="")
  TIP_CONTRA = Column(CHAR(1), default="")
  FEC_INGRES = Column(Date, default=None)
  FEC_RETIRO = Column(Date, default=None)
  FOTO = Column(CHAR(50), default="")
  FOTO1 = Column(String(50), default="")
  FIRMA = Column(CHAR(50), default="")
  NROENTREGA = Column(DECIMAL(8,0), default=0)
  NROENTPAGO = Column(DECIMAL(8,0), default=0)
  NROENTSDO = Column(DECIMAL(8,0), default=0)
  CUO_DIARIA = Column(DECIMAL(10,0), default=0)
  CTA_RENTA = Column(DECIMAL(10,0), default=0)
  CTA_SINIES = Column(DECIMAL(10,0), default=0)
  FEC_INICIO = Column(Date, default=None)
  CTADIATOTA = Column(DECIMAL(10,0), default=0)
  CTADIAPAGO = Column(DECIMAL(10,0), default=0)
  CTADIASDO = Column(DECIMAL(10,0), default=0)
  DEPO_GARAN = Column(DECIMAL(10,0), default=0)
  PAGOS = Column(DECIMAL(10,0), default=0)
  SALDO = Column(DECIMAL(10,0), default=0)
  UND_NRO = Column(CHAR(8), default="")
  UND_PRE = Column(CHAR(8), default="")
  FEC_PRESTA = Column(Date, default=None)
  FEC_DEVOLU = Column(Date, default=None)
  TURNO = Column(CHAR(2), default="")
  IMPR_CUOTA = Column(CHAR(1), default="")
  CONTR_SINI = Column(CHAR(1), default="")
  VLR_CUOTA = Column(DECIMAL(10,0), default=0)
  FEC_SINIES = Column(Date, default=None)
  NRO_CUOTAS = Column(DECIMAL(8,0), default=0)
  PAG_CUOTAS = Column(DECIMAL(8,0), default=0)
  SDO_SINIES = Column(DECIMAL(8,0), default=0)
  AHORROS = Column(DECIMAL(10,0), default=0)
  PAG_SINIES = Column(DECIMAL(10,0), default=0)
  ESTADO = Column(CHAR(1), default="")
  FEC_ESTADO = Column(Date, default=None)
  CRUCE_AHOR = Column(CHAR(16), default="")
  LICEN_NRO = Column(CHAR(12), default="")
  LICEN_CAT = Column(CHAR(2), default="")
  LICEN_VCE = Column(Date, default=None)
  DOC_TARJET = Column(CHAR(20), default="")
  FEC_TARJET = Column(Date, default=None)
  DETALLE = Column(CHAR(50), default="")
  OBSERVA = Column(CHAR(50), default="")
  CUPO = Column(DECIMAL(8,0), default=0)
  FEC_1PAGO = Column(Date, default=None)
  FEC_ULTPAG = Column(Date, default=None)
  VLR_ULTPAG = Column(DECIMAL(14,0), default=0)
  REC_ULTPAG = Column(DECIMAL(14,0), default=0)
  EX_CONDUCT = Column(Boolean, default=False)
  EX_UNIDAD = Column(Boolean, default=False)
  FEC_EXTENC = Column(Date, default=None)
  CERTI_OPER = Column(CHAR(12), default="")
  EX_CUOTAS = Column(Boolean, default=False)
  EX_VLRCTA = Column(DECIMAL(14,0), default=0)
  EX_INICIAL = Column(Boolean, default=False)
  EX_DEBITOS = Column(DECIMAL(14,0), default=0)
  EX_CREDITO = Column(DECIMAL(14,0), default=0)
  EX_SALDO = Column(DECIMAL(14,0), default=0)
  EX_AHORRO = Column(DECIMAL(14,0), default=0)
  RLAB_NOM1 = Column(CHAR(40), default="")
  RLAB_DIR1 = Column(CHAR(40), default="")
  RLAB_CIU1 = Column(CHAR(5), default="")
  RLAB_TEL1 = Column(CHAR(30), default="")
  RLAB_CAR1 = Column(CHAR(30), default="")
  RLAB_JEF1 = Column(CHAR(40), default="")
  RLAB_MOT1 = Column(CHAR(40), default="")
  RLAB_NOM2 = Column(CHAR(40), default="")
  RLAB_DIR2 = Column(CHAR(30), default="")
  RLAB_CIU2 = Column(CHAR(40), default="")
  RLAB_TEL2 = Column(CHAR(30), default="")
  RLAB_CAR2 = Column(CHAR(40), default="")
  RLAB_JEF2 = Column(CHAR(5), default="")
  RLAB_MOT2 = Column(CHAR(30), default="")
  RPER_NOM1 = Column(CHAR(40), default="")
  RPER_OCU1 = Column(CHAR(40), default="")
  RPER_DIR1 = Column(CHAR(5), default="")
  RPER_CIU1 = Column(CHAR(30), default="")
  RPER_TEL1 = Column(CHAR(40), default="")
  RPER_NOM2 = Column(CHAR(40), default="")
  RPER_OCU2 = Column(CHAR(30), default="")
  RPER_DIR2 = Column(CHAR(40), default="")
  RPER_CIU2 = Column(CHAR(5), default="")
  RPER_TEL2 = Column(CHAR(30), default="")
  RFAM_NOM1 = Column(CHAR(40), default="")
  RFAM_OCU1 = Column(CHAR(5), default="")
  RFAM_DIR1 = Column(CHAR(30), default="")
  RFAM_CIU1 = Column(CHAR(40), default="")
  RFAM_TEL1 = Column(CHAR(5), default="")
  RFAM_NOM2 = Column(CHAR(30), default="")
  RFAM_OCU2 = Column(CHAR(40), default="")
  RFAM_DIR2 = Column(CHAR(5), default="")
  RFAM_CIU2 = Column(CHAR(30), default="")
  RFAM_TEL2 = Column(CHAR(40), default="")
  RFAM_NOM3 = Column(CHAR(5), default="")
  RFAM_OCU3 = Column(CHAR(30), default="")
  RFAM_DIR3 = Column(CHAR(40), default="")
  RFAM_CIU3 = Column(CHAR(5), default="")
  RFAM_TEL3 = Column(CHAR(30), default="")
  DOCUCON = Column(CHAR(200), default="")
  DOCU00 = Column(CHAR(200), default="")
  DOCU01 = Column(CHAR(200), default="")
  DOCU02 = Column(CHAR(200), default="")
  DOCU03 = Column(CHAR(200), default="")
  DOCU04 = Column(CHAR(200), default="")
  DOCU05 = Column(CHAR(200), default="")
  DOCU06 = Column(CHAR(200), default="")
  DOCU07 = Column(CHAR(200), default="")
  DOCU08 = Column(CHAR(200), default="")
  DOCU09 = Column(CHAR(200), default="")
  LUN = Column(CHAR(1), default="")
  MAR = Column(CHAR(1), default="")
  MIE = Column(CHAR(1), default="")
  JUE = Column(CHAR(1), default="")
  VIE = Column(CHAR(1), default="")
  SAB = Column(CHAR(1), default="")
  DOM = Column(CHAR(1), default="")
  SALDO00 = Column(DECIMAL(14,0), default=0)
  SALDO01 = Column(DECIMAL(14,0), default=0)
  SALDO02 = Column(DECIMAL(14,0), default=0)
  SALDO03 = Column(DECIMAL(14,0), default=0)
  SALDO04 = Column(DECIMAL(14,0), default=0)
  SALDO05 = Column(DECIMAL(14,0), default=0)
  SALDO06 = Column(DECIMAL(14,0), default=0)
  SALDO07 = Column(DECIMAL(14,0), default=0)
  SALDO08 = Column(DECIMAL(14,0), default=0)
  SALDO09 = Column(DECIMAL(14,0), default=0)
  SALDO10 = Column(DECIMAL(14,0), default=0)
  SALDO11 = Column(DECIMAL(14,0), default=0)
  SALDO12 = Column(DECIMAL(14,0), default=0)
  FON_INSCRI = Column(CHAR(1), default="")
  FON_AHORRO = Column(CHAR(1), default="")
  DEU_RENTA = Column(DECIMAL(14,0), default=0)
  DEU_SINIES = Column(DECIMAL(14,0), default=0)
  TOTAL = Column(DECIMAL(14,0), default=0)
  FEC_CREADO = Column(Date, default=None)
  USU_CREADO = Column(CHAR(12), default="")
  USU_MODIFI = Column(CHAR(12), default="")
  EX = Column(Boolean, default=False)
  SEL = Column(Boolean, default=False)
  RECOME_NOM = Column(CHAR(50), default="")
  RECOME_CED = Column(CHAR(12), default="")
