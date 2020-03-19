from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo

crud_administrador_app = Blueprint("crud_administrador_app", __name__)

@crud_administrador_app.route('/api/crud_administrador/crear_usuario', methods=['POST'])
def crear_usuario():
    usuario = request.json['usuario']
    
    # Hacer validaciones
    usuario_a_guardar = {
        '_id': usuario['documento'],
        'nombre_usuario': usuario['nombre_usuario'],
        'documento': usuario['documento'],
        'correo': usuario['correo'],
        'contrasena': usuario['contrasena'],
        'tipo': usuario['tipo']
    }

    # despues de validar los campos que hay que validar
    try:
        mongo.db.usuarios.insert_one(usuario_a_guardar)
        return jsonify(True)
    except Exception as exception:
        print(exception)
        return jsonify(False)

@crud_administrador_app.route('/api/crud_administrador/test_traer_usuarios', methods=['GET'])
def test_traer_usuarios():
    try:
        usuarios = list(mongo.db.usuarios.find({}))
        usuarios_a_retornar = {
            'usuarios': usuarios
        }
        return jsonify(usuarios_a_retornar)
    except Exception as exception:
        return jsonify(False)
