from config.dbconnection import Base
from sqlalchemy import Column, String, Numeric, DateTime, CHAR, DECIMAL, Date, Boolean

class Conductores(Base):
  __tablename__ = "CONDUCTORES"

  CODIGO = Column(CHAR(12), primary_key=True)
  NOMBRE = Column(CHAR(50))
  CEDULA = Column(CHAR(12))
  NIT = Column(CHAR(12))
  CONTROL = Column(DECIMAL(2,0))
  CIUDAD = Column(CHAR(5))
  NOMCIUDAD = Column(CHAR(40))
  DIRECCION = Column(CHAR(120))
  TELEFONO = Column(CHAR(30))
  CELULAR = Column(CHAR(30))
  REPRESENTA = Column(CHAR(30))
  CONTACTO = Column(CHAR(40))
  TEL_CONTAC = Column(CHAR(40))
  PAR_CONTAC = Column(CHAR(20))
  CONTACTO1 = Column(CHAR(20))
  TEL_CONTA1 = Column(CHAR(40))
  PAR_CONTA1 = Column(CHAR(20))
  CONTACTO2 = Column(CHAR(20))
  TEL_CONTA2 = Column(CHAR(40))
  PAR_CONTA2 = Column(CHAR(20))
  CORREO = Column(CHAR(40))
  FEC_NACIMT = Column(Date)
  SEXO = Column(CHAR(1))
  ESTA_CIVIL = Column(CHAR(1))
  TIP_CONTRA = Column(CHAR(1))
  FEC_INGRES = Column(Date)
  FEC_RETIRO = Column(Date)
  FOTO = Column(CHAR(50))
  FOTO1 = Column(String(50))
  FIRMA = Column(CHAR(50))
  NROENTREGA = Column(DECIMAL(8,0))
  NROENTPAGO = Column(DECIMAL(8,0))
  NROENTSDO = Column(DECIMAL(8,0))
  CUO_DIARIA = Column(DECIMAL(10,0))
  CTA_RENTA = Column(DECIMAL(10,0))
  CTA_SINIES = Column(DECIMAL(10,0))
  FEC_INICIO = Column(Date)
  CTADIATOTA = Column(DECIMAL(10,0))
  CTADIAPAGO = Column(DECIMAL(10,0))
  CTADIASDO = Column(DECIMAL(10,0))
  DEPO_GARAN = Column(DECIMAL(10,0))
  PAGOS = Column(DECIMAL(10,0))
  SALDO = Column(DECIMAL(10,0))
  UND_NRO = Column(CHAR(8))
  UND_PRE = Column(CHAR(8))
  FEC_PRESTA = Column(Date)
  FEC_DEVOLU = Column(Date)
  TURNO = Column(CHAR(2))
  IMPR_CUOTA = Column(CHAR(1))
  CONTR_SINI = Column(CHAR(1))
  VLR_CUOTA = Column(DECIMAL(10,0))
  FEC_SINIES = Column(Date)
  NRO_CUOTAS = Column(DECIMAL(8,0))
  PAG_CUOTAS = Column(DECIMAL(8,0))
  SDO_SINIES = Column(DECIMAL(8,0))
  AHORROS = Column(DECIMAL(10,0))
  PAG_SINIES = Column(DECIMAL(10,0))
  ESTADO = Column(CHAR(1))
  FEC_ESTADO = Column(Date)
  CRUCE_AHOR = Column(CHAR(16))
  LICEN_NRO = Column(CHAR(2))
  LICEN_CAT = Column(CHAR(1))
  LICEN_VCE = Column(Date)
  DOC_TARJET = Column(CHAR(20))
  FEC_TARJET = Column(Date)
  DETALLE = Column(CHAR(50))
  OBSERVA = Column(CHAR(50))
  CUPO = Column(DECIMAL(8,0))
  FEC_1PAGO = Column(Date)
  FEC_ULTPAG = Column(Date)
  VLR_ULTPAG = Column(DECIMAL(14,0))
  REC_ULTPAG = Column(DECIMAL(14,0))
  EX_CONDUCT = Column(Boolean)
  EX_UNIDAD = Column(Boolean)
  FEC_EXTENC = Column(Date)
  CERTI_OPER = Column(CHAR(12))
  EX_CUOTAS = Column(Boolean)
  EX_VLRCTA = Column(DECIMAL(14,0))
  EX_INICIAL = Column(Boolean)
  EX_DEBITOS = Column(DECIMAL(14,0))
  EX_CREDITO = Column(DECIMAL(14,0))
  EX_SALDO = Column(DECIMAL(14,0))
  EX_AHORRO = Column(DECIMAL(14,0))
  RLAB_NOM1 = Column(CHAR(40))
  RLAB_DIR1 = Column(CHAR(40))
  RLAB_CIU1 = Column(CHAR(5))
  RLAB_TEL1 = Column(CHAR(30))
  RLAB_CAR1 = Column(CHAR(30))
  RLAB_JEF1 = Column(CHAR(40))
  RLAB_MOT1 = Column(CHAR(40))
  RLAB_NOM2 = Column(CHAR(40))
  RLAB_DIR2 = Column(CHAR(30))
  RLAB_CIU2 = Column(CHAR(40))
  RLAB_TEL2 = Column(CHAR(30))
  RLAB_CAR2 = Column(CHAR(40))
  RLAB_JEF2 = Column(CHAR(5))
  RLAB_MOT2 = Column(CHAR(30))
  RPER_NOM1 = Column(CHAR(40))
  RPER_OCU1 = Column(CHAR(40))
  RPER_DIR1 = Column(CHAR(5))
  RPER_CIU1 = Column(CHAR(30))
  RPER_TEL1 = Column(CHAR(40))
  RPER_NOM2 = Column(CHAR(40))
  RPER_OCU2 = Column(CHAR(30))
  RPER_DIR2 = Column(CHAR(40))
  RPER_CIU2 = Column(CHAR(5))
  RPER_TEL2 = Column(CHAR(30))
  RFAM_NOM1 = Column(CHAR(40))
  RFAM_OCU1 = Column(CHAR(5))
  RFAM_DIR1 = Column(CHAR(30))
  RFAM_CIU1 = Column(CHAR(40))
  RFAM_TEL1 = Column(CHAR(5))
  RFAM_NOM2 = Column(CHAR(30))
  RFAM_OCU2 = Column(CHAR(40))
  RFAM_DIR2 = Column(CHAR(5))
  RFAM_CIU2 = Column(CHAR(30))
  RFAM_TEL2 = Column(CHAR(40))
  RFAM_NOM3 = Column(CHAR(5))
  RFAM_OCU3 = Column(CHAR(30))
  RFAM_DIR3 = Column(CHAR(40))
  RFAM_CIU3 = Column(CHAR(5))
  RFAM_TEL3 = Column(CHAR(30))
  DOCU01 = Column(CHAR(40))
  DOCU02 = Column(CHAR(50))
  DOCU03 = Column(CHAR(50))
  DOCU04 = Column(CHAR(50))
  DOCU05 = Column(CHAR(50))
  DOCU06 = Column(CHAR(50))
  DOCU07 = Column(CHAR(50))
  DOCU08 = Column(CHAR(50))
  DOCU09 = Column(CHAR(50))
  LUN = Column(CHAR(1))
  MAR = Column(CHAR(1))
  MIE = Column(CHAR(1))
  JUE = Column(CHAR(1))
  VIE = Column(CHAR(1))
  SAB = Column(CHAR(1))
  DOM = Column(CHAR(1))
  SALDO00 = Column(DECIMAL(14,0))
  SALDO01 = Column(DECIMAL(14,0))
  SALDO02 = Column(DECIMAL(14,0))
  SALDO03 = Column(DECIMAL(14,0))
  SALDO04 = Column(DECIMAL(14,0))
  SALDO05 = Column(DECIMAL(14,0))
  SALDO06 = Column(DECIMAL(14,0))
  SALDO07 = Column(DECIMAL(14,0))
  SALDO08 = Column(DECIMAL(14,0))
  SALDO09 = Column(DECIMAL(14,0))
  SALDO10 = Column(DECIMAL(14,0))
  SALDO11 = Column(DECIMAL(14,0))
  SALDO12 = Column(DECIMAL(14,0))
  FON_INSCRI = Column(CHAR(1))
  FON_AHORRO = Column(CHAR(1))
  DEU_RENTA = Column(DECIMAL(14,0))
  DEU_SINIES = Column(DECIMAL(14,0))
  TOTAL = Column(DECIMAL(14,0))
  FEC_CREADO = Column(Date)
  USU_CREADO = Column(CHAR(12))
  USU_MODIFI = Column(CHAR(12))
  EX = Column(Boolean)
  SEL = Column(Boolean)
