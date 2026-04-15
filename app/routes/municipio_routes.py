from flask import Blueprint, request, jsonify
from ..services.municipio_service import crear_municipio, actualizar_municipio, eliminar_municipio, obtener_municipios, obtener_municipio

# Un Blueprint es como un "mini-módulo" que agrupa rutas relacionadas (en este caso, todas las rutas de municipios: crear, leer, actualizar y eliminar).
municipio_bp = Blueprint("municipios", __name__)

@municipio_bp.route("/municipios", methods=["POST"])
def crear_municipio_route():
    data = request.get_json()
    nuevo_municipio = crear_municipio(data)
    return jsonify(nuevo_municipio.to_dict()), 201


@municipio_bp.route("/municipios/<int:id>", methods=["PUT"])
def actualizar_municipio_route(id):
    data = request.get_json()
    municipio = actualizar_municipio(id, data)
    if not municipio:
        return jsonify({"error": "Municipio no encontrado"}), 404
    return jsonify(municipio.to_dict()), 200

@municipio_bp.route("/municipios/<int:id>", methods=["DELETE"])
def eliminar_municipio_route(id):
    eliminado = eliminar_municipio(id)
    if not eliminado:
        return jsonify({"error": "Municipio no encontrado"}), 404
    return jsonify({"mensaje": "Municipio eliminado correctamente"}), 200

@municipio_bp.route("/municipios", methods=["GET"])
def obtener_municipios_route():
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)
    municipios = obtener_municipios(page=page, per_page=per_page)
    return jsonify(municipios), 200

@municipio_bp.route("/municipios/<int:id>", methods=["GET"])
def obtener_municipio_route(id):
    municipio = obtener_municipio(id)
    if not municipio:
        return jsonify({"error": "Municipio no encontrado"}), 404
    return jsonify(municipio), 200