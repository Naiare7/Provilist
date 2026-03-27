from flask import Blueprint, request, jsonify
from ..services.capital_service import crear_capital

capital_bp = Blueprint("capitales", __name__)

@capital_bp.route("/capitales", methods=["POST"])
def crear_capital_route():
    data = request.get_json()
    nueva_capital = crear_capital(data)
    return jsonify(nueva_capital.to_dict()), 201
