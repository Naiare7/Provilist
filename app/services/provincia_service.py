from ..models import Provincia
from .. import db

def crear_provincia(data):
    nueva_provincia = Provincia(
        nombre=data["nombre"],
        pais=data["pais"],
        codigo=data["codigo"],
        tiene_municipio=data["tiene_municipio"]
    )
    db.session.add(nueva_provincia)
    db.session.commit()
    return nueva_provincia

def actualizar_provincia(id, data):
    provincia = Provincia.query.get(id)
    if not provincia:
        return None
    provincia.nombre = data.get("nombre", provincia.nombre)
    provincia.pais = data.get("puesto", provincia.pais)
    provincia.codigo = data.get("codigo", provincia.codigo)
    provincia.tiene_municipio = data.get("tiene_municipio", provincia.tiene_municipio)
    db.session.commit()
    return provincia

def eliminar_provincia(id):
    provincia = Provincia.query.get(id)
    if not provincia:
        return False
    db.session.delete(provincia)
    db.session.commit()
    return True

def obtener_provincias():
    provincias = Provincia.query.all()
    return [p.to_dict() for p in provincias]
