from app.models import Capital
from app import db

capitales_seed = [
    {"nombre": "Bilbao", "codigo_de_provincia":"BI", "latitud": 43.26271, "longitud": -2.92528},
    {"nombre": "Donostia-San Sebastián", "codigo_de_provincia":"GI", "latitud": 43.31283, "longitud": -1.97499},
    {"nombre": "Vitoria-Gasteiz", "codigo_de_provincia":"AL", "latitud": 42.84998, "longitud": -2.67268},
    {"nombre": "Pamplona - Iruña", "codigo_de_provincia":"NA", "latitud": 42.81687, "longitud": -1.64323},
    {"nombre": "Bayonne - Baiona", "codigo_de_provincia":"LP", "latitud": 43.49316, "longitud": -1.473},
    {"nombre": "Mauleón - Maule-Lextarre", "codigo_de_provincia":"ZU", "latitud": 43.22422, "longitud": -0.88717},
    {"nombre": "Saint-Jean-Pied-de-Port - Donibane Garazi", "codigo_de_provincia":"BN", "latitud": 43.16473, "longitud": -1.23729}
]

def seed_capitales():
    for data in capitales_seed:
        #evitar duplicados
        existe = Capital.query.filter_by(nombre=data["nombre"]).first()
        if existe:
            existe.nombre = data["nombre"]
            existe.codigo_provincia = data["codigo_de_provincia"]
            existe.latitud = data["latitud"]
            existe.longitud = data["longitud"]
            # db.session.commit()
        else:
            capital = Capital(
            nombre=data["nombre"],
            codigo_provincia=data["codigo_de_provincia"],
            latitud=data["latitud"],
            longitud=data["longitud"])

            db.session.add(capital)
        

    db.session.commit()