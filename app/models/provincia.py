from .. import db
from .base import BaseMixin

class Provincia(db.Model, BaseMixin):
    __tablename__ = "provincias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(10), nullable=False)
    codigo = db.Column(db.String(2), nullable=False, unique=True)
    tiene_municipio = db.Column(db.Boolean, nullable=False, default=False)
    
    # Relación: Una Provincia tiene capitales 
    # Usamos back_populates para mayor claridad (opcional pero profesional)
    capital = db.relationship('Capital', backref='Provincia', primaryjoin="Provincia.codigo==Capital.codigo_provincia", lazy=True, cascade="all, delete")
    
    # Relación: Una Provincia tiene muchos municipios 
    municipio = db.relationship('Municipio', backref='Provincia', lazy=True, cascade="all, delete")
