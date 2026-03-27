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
