from flask import Blueprint, request, jsonify
from .models import Provincia, Municipio, Capital

from . import db

main = Blueprint("main", __name__)

# --- RUTA HOME ---
@main.route("/")
def home():
    return {"mensaje": "API funcionando"}

# RUTAS PROVINCIAS
@main.route("/provincias", methods=["POST"])
def crear_provincias ():
    data = request.get_json()
    nueva_provincia = Provincia (
        nombre = data["nombre"],
        pais = data["pais"],
        codigo = data["codigo"],
        tiene_municipio = data["tiene_municipio"]
        )
    
    db.session.add(nueva_provincia)
    db.session.commit()
    return jsonify(nueva_provincia.to_dict()), 201


@main.route("/provincias/<int:id>", methods=["PUT"])
def actualizar_provincia(id):
    data = request.get_json()
    
    provincia = Provincia.query.get(id)
    
    if not provincia:
        return jsonify({"error": "Empleado no encontrado"}), 404

    # Actualización de campos (solo si vienen en el JSON)
    provincia.nombre = data.get("nombre", provincia.nombre)
    provincia.pais = data.get("puesto", provincia.pais)
    provincia.codigo = data.get("codigo", provincia.codigo)
    provincia.tiene_municipio = data.get("tiene_municipio", provincia.tiene_municipio)

    db.session.commit()

    return jsonify(provincia.to_dict()), 200

@main.route("/provincias/<int:id>", methods=["DELETE"])
def eliminar_provincia(id):
    provincia = Provincia.query.get(id)

    if not provincia:
        return jsonify({"error": "Provincia no encontrado"}), 404

    db.session.delete(provincia)
    db.session.commit()

    return jsonify({"mensaje": "Provincia eliminada correctamente"}), 200

# Rutas Municipios
@main.route("/municipios", methods=["POST"])
def crear_municipio ():
    data = request.get_json()
    nuevo_municipio = Municipio (
        nombre = data["nombre"],
        provincia_id = data ["provincia_id"],
        codigo_postal = data ["codigo_postal"],
        poblacion = data ["poblacion"],
        area_km2 = data ["area_km2"],
        latitud = data ["latitud"],
        longitud = data ["longitud"],
        created_at = data ["create_at"],
        updated_at = data ["updated_at"]      
        )
    
    db.session.add(nuevo_municipio)
    db.session.commit()
    return jsonify(nuevo_municipio.to_dict()), 201

@main.route("/capitales", methods=["POST"])
def crear_capital ():
    data = request.get_json()
    nueva_capital = Capital (
        nombre = data["nombre"],
        provincia_id = data ["provincia_id"],
        latitud = data ["latitud"],
        longitud = data ["longitud"]
      
        )
    
    db.session.add(nueva_capital)
    db.session.commit()
    return jsonify(nueva_capital.to_dict()), 201

