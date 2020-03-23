from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo

crud_administrador_app = Blueprint("crud_administrador_app", __name__)

@crud_administrador_app.route('/api/crud_administrador/crear_usuario', methods=['POST'])
def crear_usuario():
    usuario = request.json['usuario']

    mensaje = {"tipo": "", "mensaje": ""}

    if validar_cedula(usuario['cedula']):
        if validar_correo(usuario['correo']):
            if validar_usuario(usuario['usuario']):
                if validacion_contrasena_segura(usuario['contrasena']): 
                    try:

                        guardar_usuario(usuario)

                        mensaje["tipo"] = "aprobado"
                        mensaje["mensaje"] = "Usuario creado con exito"
                        return jsonify(mensaje)
                    except Exception as exception:
                        print("======REG_U_NUEVO=====")
                        print(exception)
                        mensaje["tipo"] = "error_interno"
                        mensaje["mensaje"] = "Error en la conexion con la base de datos"
                        return jsonify(mensaje)
                else:
                    mensaje["tipo"] = "error_contrasena"
                    mensaje["mensaje"] = "La contrasena no cumple con las medidas de seguridad"
                    return jsonify(mensaje)
            else:
                mensaje["tipo"] = "error_nombre_usuario"
                mensaje["mensaje"] = "Nombre de usuario ya existe"
                return jsonify(mensaje)
        else:
            mensaje["tipo"] = "error_correo"
            mensaje["mensaje"] = "Correo ya registrado"
            return jsonify(mensaje)
    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "Documento ya registrado"
        return jsonify(mensaje)

def guardar_usuario(usuario):
    contrasena_hash = contrasena_md5(usuario['contrasena'])
    usuario_a_guardar = {
        '_id': usuario['documento'],
        'nombre_usuario': usuario['nombre_usuario'],
        'documento': usuario['documento'],
        'correo': usuario['correo'],
        'contrasena': contrasena_hash,
        'tipo': usuario['tipo'],
        'puntos': 0,
        'arboles': [],
        'km_recorridos': 0,
        'dias_uso_cv': 0,
        'dias_uso_cr': 0,
        'tiempo_uso_cv': 0,
        'tiempo_uso_cr': 0,
        'tareas_realizadas': []
    }
    mongo.db.usuarios.insert_one(usuario_a_guardar)

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