from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo
from project.validaciones_usuario.validaciones_existencia_usuario import validar_existencia_documento

utilidades_administrador_app = Blueprint("utilidades_administrador_app", __name__)


@utilidades_administrador_app.route('/api/crud_administrador/traer_usuarios', methods=['GET'])
def traer_usuarios():
    try:
        mensaje = {"tipo": "", "mensaje": ""}

        usuarios = list(mongo.db.usuarios.find({}))

        usuarios_a_retornar = retirar_info_usuarios(usuarios)
        
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = usuarios_a_retornar

        return jsonify(mensaje)
    except Exception as exception:
        print("======USUARIOS=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

def retirar_info_usuarios(usuarios):
    usuarios_a_retornar = []
    for usu in usuarios:
        usuario = {
            'nombre_usuario' : '',
            'documento': '',
            'imagen': ''
        }
        usuario['nombre_usuario'] = usu['nombre_usuario']
        usuario['documento'] = usu['documento']
        usuario['imagen'] = usu['imagen']

        usuarios_a_retornar.append(usuario)
    return usuarios_a_retornar


@utilidades_administrador_app.route('/api/crud_administrador/traer_datos_usuario', methods=['GET'])
def traer_datos_usuario():
    documento = request.args['documento']

    mensaje = {"tipo": "", "mensaje": ""}
    if validar_existencia_documento(documento) == False:
        try:
            datos_usuario = list(mongo.db.usuarios.find({'documento': documento}))[0]
            datos_usuario_limpio = retirar_datos_usuario(datos_usuario)

            mensaje["tipo"] = "aprobado"
            mensaje["mensaje"] = datos_usuario_limpio
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

def retirar_datos_usuario(datos_usuario):
    usuario = {
        'nombre_usuario': datos_usuario['nombre_usuario'],
        'documento': datos_usuario['documento'],
        'correo': datos_usuario['correo'],
        'tipo': datos_usuario['tipo'],
        'imagen': datos_usuario['imagen']
    }
    return usuario
