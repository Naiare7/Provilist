from ..models import Municipio
from .. import db

def crear_municipio(data):
    nuevo_municipio = Municipio(
        nombre=data["nombre"],
        provincia_id=data["provincia_id"],
        codigo_postal=data["codigo_postal"],
        poblacion=data["poblacion"],
        area_km2=data["area_km2"],
        latitud=data["latitud"],
        longitud=data["longitud"],
        created_at=data["create_at"],
        updated_at=data["updated_at"]
    )
    db.session.add(nuevo_municipio)
    db.session.commit()
    return nuevo_municipio

def actualizar_municipio(id, data):
    municipio = Municipio.query.get(id)
    if not municipio:
        return None
    municipio.nombre = data.get("nombre", municipio.nombre)
    municipio.provincia_id = data.get("provincia_id", municipio.provincia_id)
    municipio.codigo_postal = data.get("codigo_postal", municipio.codigo_postal)
    municipio.poblacion = data.get("poblacion", municipio.poblacion)
    municipio.area_km2 = data.get("area_km2", municipio.area_km2)
    municipio.latitud = data.get("latitud", municipio.latitud)
    municipio.longitud = data.get("longitud", municipio.longitud)
    db.session.commit()
    return municipio

def eliminar_municipio(id):
    municipio = Municipio.query.get(id)
    if not municipio:
        return False
    db.session.delete(municipio)
    db.session.commit()
    return True

def obtener_municipios():
    municipios = Municipio.query.all()
    return [m.to_dict() for m in municipios]

def obtener_municipio(id):
    municio = Municipio.query.get(id)
    if not municio:
        return False
    return municio.to_dict()
