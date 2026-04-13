from flask import Blueprint, request, jsonify
from ..services.capital_service import crear_capital, actualizar_capital, eliminar_capital, obtener_capitales, obtener_capital

capital_bp = Blueprint("capitales", __name__)

@capital_bp.route("/capitales", methods=["POST"])
def crear_capital_route():
    data = request.get_json()
    nueva_capital = crear_capital(data)
    return jsonify(nueva_capital.to_dict()), 201

@capital_bp.route("/capitales/<int:id>", methods=["PUT"])
def actualizar_capital_route(id):
    data= request.get_json()
    capital = actualizar_capital(id, data)
    if not capital:
        return jsonify({"error": "Capital no encontrada"}), 404
    return jsonify(capital.to_dict()), 200

@capital_bp.route("/capitales/<int:id>", methods= ["DELETE"])
def eliminar_capitales_route(id):
    eliminada = eliminar_capital(id)
    if not eliminada:
        return jsonify({"error": "Capital no encontrado"}), 404
    return jsonify({"mensaje": "Capital eliminada correctamente"}), 200

@capital_bp.route("/capitales", methods=["GET"])
def obtener_capitales_route():
    capitales = obtener_capitales()
    return jsonify(capitales), 200

@capital_bp.route("/capitales/<int:id>", methods=["GET"])
def obtener_capital_route(id):
    capital = obtener_capital(id)
    if not capital:
        return jsonify({"error": "Capital no encontrada"}), 404
    return jsonify(capital), 200