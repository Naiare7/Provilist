from .provincia import Provincia
from .capital import Capital
from .municipio import Municipio

# Esto facilita la importación en otros archivos de la app:
# from app.models import Provincia, Capital, Municipio
__all__ = ["Provincia", "Capital", "Municipio"]
