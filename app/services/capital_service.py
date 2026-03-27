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
