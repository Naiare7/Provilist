from flask import Blueprint, request, jsonify
from ..services.provincia_service import crear_provincia, actualizar_provincia, eliminar_provincia, obtener_provincias, obtener_provincia

provincia_bp = Blueprint("provincias", __name__)

@provincia_bp.route("/provincias", methods=["POST"])
def crear_provincias_route():
    data = request.get_json()
    nueva_provincia = crear_provincia(data)
    return jsonify(nueva_provincia.to_dict()), 201

@provincia_bp.route("/provincias/<int:id>", methods=["PUT"])
def actualizar_provincia_route(id):
    data = request.get_json()
    provincia = actualizar_provincia(id, data)
    if not provincia:
        return jsonify({"error": "Provincia no encontrada"}), 404
    return jsonify(provincia.to_dict()), 200

@provincia_bp.route("/provincias/<int:id>", methods=["DELETE"])
def eliminar_provincia_route(id):
    eliminada = eliminar_provincia(id)
    if not eliminada:
        return jsonify({"error": "Provincia no encontrado"}), 404
    return jsonify({"mensaje": "Provincia eliminada correctamente"}), 200

@provincia_bp.route("/provincias", methods=["GET"])
def obtener_provincias_route():
    provincias = obtener_provincias()
    return jsonify(provincias), 200

@provincia_bp.route("/provincias/<int:id>", methods=["GET"])
def obtener_provincia_route(id):
    provincia = obtener_provincia(id)
    if not provincia:
        return jsonify({"error": "Provincia no encontrada"}), 404
    return jsonify(provincia), 200