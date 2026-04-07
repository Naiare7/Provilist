from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Instanciamos la base de datos sin vincularla aún a la app
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Vinculamos la base de datos con nuestra app configurada
    db.init_app(app)
    migrate.init_app(app, db) 
    CORS(app)

    # Importamos y registramos las rutas
    from .routes import main, provincia_bp, municipio_bp, capital_bp
    app.register_blueprint(main)
    app.register_blueprint(provincia_bp)
    app.register_blueprint(municipio_bp)
    app.register_blueprint(capital_bp)

    # Registro de comandos CLI
    from .seeds import run_seeds
    @app.cli.command("seed")
    def seed():
        """Ejecuta los seeds"""
        run_seeds()
        print("Seeds ejecutados correctamente")

    return app