from .provincia import Provincia
from .capital import Capital
from .municipio import Municipio
from .user import User

# Esto facilita la importación en otros archivos de la app:
# from app.models import Provincia, Capital, Municipio, User
__all__ = ["Provincia", "Capital", "Municipio", "User"]
