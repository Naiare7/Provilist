import os

class Config:
    # Obtiene la ruta absoluta de la carpeta actual
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define dónde se guardará el archivo SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../provilist.db')
    
    # Desactiva una función de SQLAlchemy que consume mucha memoria
    SQLALCHEMY_TRACK_MODIFICATIONS = False