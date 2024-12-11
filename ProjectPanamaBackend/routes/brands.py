from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.dbconnection import session
from models.marcas import Marcas
from fastapi.encoders import jsonable_encoder

brands_router = APIRouter()

@brands_router.get("/brands", tags=["Brands"])
async def get_brands():
  db = session()
  try:
    brands = db.query(Marcas.CODIGO, Marcas.NOMBRE).all()
    brands = [{'codigo': brand.CODIGO, 'nombre': brand.NOMBRE} for brand in brands]
    return JSONResponse(content=jsonable_encoder(brands), status_code=200)
  except Exception as e:
    return JSONResponse(content=jsonable_encoder({'error': str(e)}), status_code=500)
  finally:
    db.close()