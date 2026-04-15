from app.models import Provincia
from app import db

provincias_seed = [
    {"nombre": "Bizkaia", "pais": "Euskal Herria", "codigo": "BI", "tiene_municipio": True},
    {"nombre": "Gipuzkoa", "pais": "Euskal Herria", "codigo": "GI", "tiene_municipio": True},
    {"nombre": "Álava", "pais": "Euskal Herria", "codigo": "AL", "tiene_municipio": True},
    {"nombre": "Navarra", "pais": "Euskal Herria", "codigo": "NA", "tiene_municipio": True},
    {"nombre": "Lapurdi", "pais": "Euskal Herria", "codigo": "LP", "tiene_municipio": False},
    {"nombre": "Zuberoa", "pais": "Euskal Herria", "codigo": "ZU", "tiene_municipio": False},
    {"nombre": "Baja Navarra", "pais": "Euskal Herria", "codigo": "BN", "tiene_municipio": False},
]

def seed_provincias():
    for data in provincias_seed:
        # evitar duplicados
        existe = Provincia.query.filter_by(codigo=data["codigo"]).first()
        if existe:
            existe.nombre = data["nombre"]
            existe.pais = data["pais"]
            existe.codigo = data["codigo"]
            existe.tiene_municipio = data["tiene_municipio"]

        else:

            provincia = Provincia(
                nombre=data["nombre"],
                pais=data["pais"],
                codigo=data["codigo"],
                tiene_municipio=data["tiene_municipio"]
            )

            db.session.add(provincia)

    db.session.commit()