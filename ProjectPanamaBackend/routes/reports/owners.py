from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.dbconnection import session
from models.propietarios import Propietarios
from models.vehiculos import Vehiculos
from schemas.reports import *
from fastapi.encoders import jsonable_encoder
from utils.reports import *
from datetime import datetime
import pytz

from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import jinja2
from utils.pdf import html2pdf

templateJinja = Jinja2Templates(directory="templates")

ownersReports_router = APIRouter()

@ownersReports_router.get('/directorio-propietarios')
async def get_propietarios_detalles():
    db = session()
    try:
        propietarios_detalles = db.query(
            Propietarios.ESTADO.label('propietario_estado'),
            Propietarios.CODIGO.label('propietario_codigo'),
            Propietarios.NOMBRE.label('propietario_nombre'),
            Propietarios.CIUDAD.label('propietario_ciudad'),
            Propietarios.DIRECCION.label('propietario_direccion'),
            Propietarios.TELEFONO.label('propietario_telefono'),
            Propietarios.CELULAR.label('propietario_celular'),
            Propietarios.CORREO.label('propietario_correo'),
        )  .all()
        
        # Convertir los resultados en un formato JSON
        propietarios_detalles_list = []
        for resultado in propietarios_detalles:
            propietario_detalle = {
                'propietario_estado': resultado.propietario_estado,
                'propietario_codigo': resultado.propietario_codigo,
                'propietario_nombre': resultado.propietario_nombre,
                'propietario_ciudad': resultado.propietario_ciudad,
                'propietario_direccion': resultado.propietario_direccion,
                'propietario_telefono': resultado.propietario_telefono,
                'propietario_celular': resultado.propietario_celular,
                'propietario_correo': resultado.propietario_correo
            }
            propietarios_detalles_list.append(propietario_detalle)
    
        data = agrupar_empresas_por_estado(propietarios_detalles_list)

        # Datos de la fecha y hora actual
        # Define la zona horaria de Ciudad de Panamá
        panama_timezone = pytz.timezone('America/Panama')
        # Obtén la hora actual en la zona horaria de Ciudad de Panamá
        now_in_panama = datetime.now(panama_timezone)
        # Formatea la fecha y la hora según lo requerido
        fecha = now_in_panama.strftime("%d/%m/%Y")
        hora_actual = now_in_panama.strftime("%I:%M:%S %p")
        usuario = "admin" 
        titulo = 'Directorio Propietarios'

        # Inicializar el diccionario data_view con información común
        data_view = {
            "fecha": fecha,
            "hora": hora_actual
        }

        for estado, info in data.items():
            if isinstance(info, dict):
                estado_nombre = info.pop('nombre_estado', 'Sin nombre')
                data_view[estado] = {
                    "nombre_estado": estado_nombre,
                    "empresas": []
                }
                for empresa_codigo, empresa_info in info.items():
                    if isinstance(empresa_info, dict):
                        empresa = {
                            "codigo_empresa": empresa_info.get("propietario_codigo", ""),
                            "nombre": empresa_info.get("propietario_nombre", ""),
                            "ciudad": empresa_info.get("propietario_ciudad", ""),
                            "direccion": empresa_info.get("propietario_direccion", ""),
                            "telefono": empresa_info.get("propietario_telefono", ""),
                            "celular": empresa_info.get("propietario_celular", ""),
                            "correo": empresa_info.get("propietario_correo", ""),
                        }
                        data_view[estado]["empresas"].append(empresa)
        
        data_view["usuario"] = usuario

        headers = {
            "Content-Disposition": "inline; directorio-propietarios.pdf"
        }  

        template_loader = jinja2.FileSystemLoader(searchpath="./templates")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = "DirectorioPropietarios.html"
        header_file = "header.html"
        footer_file = "footer.html"
        template = template_env.get_template(template_file)
        header = template_env.get_template(header_file)
        footer = template_env.get_template(footer_file)
        output_text = template.render(data_view=data_view)
        output_header = header.render(data_view=data_view)
        output_footer = footer.render(data_view=data_view)

        html_path = f'./templates/renderDirectorioPropietarios.html'
        header_path = f'./templates/renderheader.html'
        footer_path = f'./templates/renderfooter.html'
        html_file = open(html_path, 'w')
        header_file = open(header_path, 'w')
        html_footer = open(footer_path, 'w') 
        html_file.write(output_text)
        header_file.write(output_header)
        html_footer.write(output_footer) 
        html_file.close()
        header_file.close()
        html_footer.close()
        pdf_path = 'propietarios-detalles.pdf'
        html2pdf(titulo, html_path, pdf_path, header_path=header_path, footer_path=footer_path)

        response = FileResponse(pdf_path, media_type='application/pdf', filename='templates/propietarios-detalles.pdf', headers=headers)
        
        return response

        #return JSONResponse(content=jsonable_encoder(data))
    finally:
        db.close()

#--------------------------------------------------------------------------------

@ownersReports_router.post('/valor-compra-vehiculos', response_class=FileResponse)
async def get_vehiculos_detalles(infoReports: infoReports):
    db = session()
    try:
        vehiculos_detalles = db.query(
            Vehiculos.PROPI_IDEN.label('propietario_codigo'),
            Vehiculos.EMPRESA.label('vehiculo_empresa'),
            Vehiculos.NUMERO.label('vehiculo_unidad'),
            Vehiculos.PLACA.label('vehiculo_placa'),
            Vehiculos.NOMMARCA.label('vehiculo_marca'),
            Vehiculos.LINEA.label('vehiculo_linea'),
            Vehiculos.MODELO.label('vehiculo_modelo'),
            Vehiculos.NRO_CUPO.label('vehiculo_cupo'),
            Vehiculos.MOTORNRO.label('vehiculo_motor'),
            Vehiculos.CHASISNRO.label('vehiculo_chasis'),
            Vehiculos.NOMESTADO.label('vehiculo_estado'),
            Vehiculos.FAC_COMPRA.label('vehiculo_factura_compra'),
            Vehiculos.FEC_COMPRA.label('vehiculo_fecha_compra'),
            Vehiculos.VLR_COMPRA.label('vehiculo_valor_compra')
        ).filter(
            Vehiculos.PROPI_IDEN.in_(infoReports.empresas),
            Vehiculos.ESTADO.in_(infoReports.estados)
        ).all()

        vehiculos_detalles_list = []
        for result in vehiculos_detalles:
            vehiculo_detalle = {
                'propietario_codigo': result.propietario_codigo,
                'vehiculo_empresa': result.vehiculo_empresa,
                'vehiculo_unidad': result.vehiculo_unidad,
                'vehiculo_placa': result.vehiculo_placa,
                'vehiculo_marca': result.vehiculo_marca,
                'vehiculo_linea': result.vehiculo_linea,
                'vehiculo_modelo': result.vehiculo_modelo,
                'vehiculo_cupo': result.vehiculo_cupo,
                'vehiculo_motor': result.vehiculo_motor,
                'vehiculo_chasis': result.vehiculo_chasis,
                'vehiculo_estado': result.vehiculo_estado,
                'vehiculo_factura_compra': result.vehiculo_factura_compra,
                'vehiculo_fecha_compra': result.vehiculo_fecha_compra,
                'vehiculo_valor_compra': result.vehiculo_valor_compra,
            }
            vehiculos_detalles_list.append(vehiculo_detalle)

        data = valor_compra_vehiculos(vehiculos_detalles_list)

        # Datos de la fecha y hora actual
        # Define la zona horaria de Ciudad de Panamá
        panama_timezone = pytz.timezone('America/Panama')
        # Obtén la hora actual en la zona horaria de Ciudad de Panamá
        now_in_panama = datetime.now(panama_timezone)
        # Formatea la fecha y la hora según lo requerido
        fecha = now_in_panama.strftime("%d/%m/%Y")
        hora_actual = now_in_panama.strftime("%I:%M:%S %p")
        usuario = infoReports.usuario
        titulo = 'Valor Compra de Vehículos'

        data_view = {
            "fecha": fecha,
            "hora": hora_actual,
            "usuario": usuario,
            "propietarios": []
        }

        for propietario_codigo, info in data.items():
            if isinstance(info, dict):
                propietario_data = {
                    "codigo_empresa": info.get("propietario_codigo", ""),
                    "nombre_empresa": info.get("vehiculo_empresa", ""),
                    "empty": info.get("empty", ""),
                    "vehiculos": []
                }
                for vehiculo_codigo, vehiculo_info in info.get("vehiculos", {}).items():
                    if isinstance(vehiculo_info, dict):
                        vehiculo_data = {
                            "vehiculo_unidad": vehiculo_info.get("vehiculo_unidad", ""),
                            "vehiculo_placa": vehiculo_info.get("vehiculo_placa", ""),
                            "vehiculo_marca": vehiculo_info.get("vehiculo_marca", ""),
                            "vehiculo_linea": vehiculo_info.get("vehiculo_linea", ""),
                            "vehiculo_modelo": vehiculo_info.get("vehiculo_modelo", ""),
                            "vehiculo_cupo": vehiculo_info.get("vehiculo_cupo", ""),
                            "vehiculo_motor": vehiculo_info.get("vehiculo_motor", ""),
                            "vehiculo_chasis": vehiculo_info.get("vehiculo_chasis", ""),
                            "vehiculo_estado": vehiculo_info.get("vehiculo_estado", ""),
                            "vehiculo_valor_compra": vehiculo_info.get("vehiculo_valor_compra", ""),
                            "vehiculo_factura": vehiculo_info.get("vehiculo_factura", ""),
                            "vehiculo_fecha_compra": vehiculo_info.get("vehiculo_fecha_compra", "")
                        }
                        propietario_data["vehiculos"].append(vehiculo_data)
                data_view["propietarios"].append(propietario_data)

        data_view["usuario"] = usuario

        headers = {
            "Content-Disposition": "inline; valor-compra-vehiculos.pdf"
        }

        template_loader = jinja2.FileSystemLoader(searchpath="./templates")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = "ValorCompraVehiculos.html"
        header_file = "header.html"
        footer_file = "footer.html"
        template = template_env.get_template(template_file)
        header = template_env.get_template(header_file)
        footer = template_env.get_template(footer_file)
        output_text = template.render(data_view=data_view)
        output_header = header.render(data_view=data_view)
        output_footer = footer.render(data_view=data_view)
        
        html_path = f'./templates/renderValorCompraVehiculos.html'
        header_path = f'./templates/renderheader.html'
        footer_path = f'./templates/renderfooter.html'
        html_file = open(html_path, 'w')
        header_file = open(header_path, 'w')
        html_footer = open(footer_path, 'w')
        html_file.write(output_text)
        header_file.write(output_header)
        html_footer.write(output_footer)
        html_file.close()
        header_file.close()
        html_footer.close()
        pdf_path = 'valor-compra-vehiculos.pdf'
        html2pdf(titulo, html_path, pdf_path, header_path=header_path, footer_path=footer_path)

        response = FileResponse(pdf_path, media_type='application/pdf', filename='templates/valor-compra-vehiculos.pdf', headers=headers)

        return response

        return JSONResponse(content=jsonable_encoder(data))
    
    finally:
        db.close()