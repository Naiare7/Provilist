from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {"mensaje": "API funcionando"}

from .provincia_routes import provincia_bp
from .municipio_routes import municipio_bp
from .capital_routes import capital_bp
