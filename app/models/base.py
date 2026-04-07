from datetime import datetime
from decimal import Decimal
from .. import db

class BaseMixin:
    """Mixin para añadir funcionalidad común a los modelos (como to_dict)."""
    
    def to_dict(self):
        """Convierte las columnas del modelo en un diccionario."""
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
        # Manejo especial para objetos datetime y decimales
        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            elif isinstance(value, Decimal):
                result[key] = float(value)
        
        return result

class TimestampMixin:
    """Mixin para añadir campos de auditoría temporal."""
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
