from .. import db
from .base import BaseMixin

class Capital(db.Model, BaseMixin):
    __tablename__ = "capitales"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo_provincia = db.Column(db.String(2), db.ForeignKey('provincias.codigo'), nullable=False) 
    latitud = db.Column(db.Numeric(9,6), nullable=True)
    longitud = db.Column(db.Numeric(9,6), nullable=True)

    def to_dict(self):
        # Usamos la base para los campos de la tabla
        data = super().to_dict()
        
        # Añadimos el campo extra que existía originalmente
        # Check para evitar errores si la relación no está cargada (aunque suele estarlo)
        if self.Provincia:
            data["nombre_provincia"] = self.Provincia.nombre
            
        return data
