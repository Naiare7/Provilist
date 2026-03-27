from . import db
from datetime import datetime

class Provincia(db.Model):
    __tablename__ = "provincias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(10), nullable=False)
    codigo = db.Column(db.String(2), nullable=False, unique=True)
    tiene_municipio = db.Column(db.Boolean, nullable=False, default=False)
    
    # Relación: Una Provincia tiene capitales 
    capital = db.relationship('Capital', backref='Provincia', lazy=True)
    # Relación: Una Provincia tiene muchos municipios 
    municipio = db.relationship('Municipio', backref='Provincia', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "pais": self.pais,
            "codigo": self.codigo,
            "tiene_municipio": self.tiene_municipio
        }

class Capital(db.Model):
    __tablename__ = "capitales"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.String(2), db.ForeignKey('provincias.id'), nullable=False) 
    latitud = db.Column(db.Numeric(9,6), nullable=True)
    longitud = db.Column(db.Numeric(9,6), nullable=True)



    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia_id": self.provincia_id,
            "nombre_provincia": self.Provincia.nombre,
            "latitud": self.latitud,
            "longitud": self.longitud
        }

class Municipio (db.Model):
    __tablename__ = "municipios"
     
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincias.id'), nullable=False) 
    codigo_postal = db.Column(db.Integer, nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    area_km2 = db.Column(db.Numeric(10,2))
    latitud = db.Column(db.Numeric(9,6), nullable=True)
    longitud = db.Column(db.Numeric(9,6), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
     
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia_id": self.provincia_id,
            "nombre_provincia": self.Provincia.nombre,
            "codigo_postal": self.codigo_postal,
            "poblacion": self.poblacion,
            "area_km2": self.area_km2,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

     
