from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo

utilidades_administrador_app = Blueprint("utilidades_administrador_app", __name__)


@utilidades_administrador_app.route('/api/crud_administrador/traer_usuarios', methods=['GET'])
def traer_usuarios():
    try:
        usuarios = list(mongo.db.usuarios.find({}))

        usuarios_a_retornar = retirar_info_usuarios(usuarios)

        return jsonify(usuarios_a_retornar)
    except Exception as exception:
        print("======USUARIOS=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

def retirar_info_usuarios(usuarios):
    usuario = {
        'nombre_usuario' : '',
        'documento': ''
    }
    usuarios_a_retornar = []
    for usu in usuarios:
        usuario['nombre_usuario'] = usu['nombre_usuario']
        usuario['documento'] = usu['documento']
        
        usuarios_a_retornar.append(usuario)
    return usuarios_a_retornar


@utilidades_administrador_app.route('/api/crud_administrador/traer_datos_usuario', methods=['GET'])
def traer_datos_usuario():
    usuario = request.json['usuario']

    mensaje = {"tipo": "", "mensaje": ""}
    if validar_existencia_documento(nombre_usuario) == False:
        try:

            datos_usuario = mongo.db.usuarios.find({'_id': usuario['documento']})

            datos_usuario['contrasena'] = ''

            mensaje["tipo"] = "usuario"
            mensaje["mensaje"] = datos_usuario
            return jsonify(mensaje)
        except Exception as exception:
            print("======DATOS_USUA=====")
            print(exception)
            mensaje["tipo"] = "error_interno"
            mensaje["mensaje"] = "Error en la conexion con la base de datos"
            return jsonify(mensaje)

    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuaio no se encuentra registrado"
        return jsonify(mensaje)
