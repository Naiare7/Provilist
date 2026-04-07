from .. import db
from .base import BaseMixin, TimestampMixin

class Municipio(db.Model, BaseMixin, TimestampMixin):
    __tablename__ = "municipios"
     
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincias.id'), nullable=False) 
    codigo_postal = db.Column(db.Integer, nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    area_km2 = db.Column(db.Numeric(10,2))
    latitud = db.Column(db.Numeric(9,6), nullable=True)
    longitud = db.Column(db.Numeric(9,6), nullable=True)

    def to_dict(self):
        # Usamos la base para los campos de la tabla
        data = super().to_dict()
        
        # Añadimos el nombre de la provincia
        if self.Provincia:
            data["nombre_provincia"] = self.Provincia.nombre
            
        return data
