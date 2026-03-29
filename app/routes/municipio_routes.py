from flask import Blueprint, request, jsonify
from ..services.municipio_service import crear_municipio

municipio_bp = Blueprint("municipios", __name__)

@municipio_bp.route("/municipios", methods=["POST"])
def crear_municipio_route():
    data = request.get_json()
    nuevo_municipio = crear_municipio(data)
    return jsonify(nuevo_municipio.to_dict()), 201
