from ..models import Capital
from .. import db

def crear_capital(data):
    nueva_capital = Capital(
        nombre=data["nombre"],
        provincia_id=data["provincia_id"],
        latitud=data["latitud"],
        longitud=data["longitud"]
    )
    db.session.add(nueva_capital)
    db.session.commit()
    return nueva_capital

def actualizar_capital(id, data):
    capital = Capital.query.get(id)
    if not capital:
        return None
    capital.nombre = data.get("nombre", capital.nombre)
    capital.codigo_provincia = data.get("codigo_provincia", capital.provincia_id)
    capital.latitud = data.get ("latitud", capital.latitud)
    capital.longitud = data.get ("longitud", capital.longitud)

def eliminar_capital(id):
    capital = Capital.query.get(id)
    if not capital:
        return False
    db.session.delete(capital)
    db.session.commit()
    return True

def obtener_capitales():
    capitales = Capital.query.all()
    return [p.to_dict() for p in capitales]