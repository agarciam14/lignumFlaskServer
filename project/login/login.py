from flask import jsonify
from flask import request
from flask import Blueprint
import json
import hashlib

from project import mongo

login_app = Blueprint("login_app", __name__)

@login_app.route('/api/login', methods=['POST'])
def login():
    usuario = request.json['usuario']

    nombre_usuario = usuario['usuario']
    contrasena = usuario['contrasena']

    mensaje = {"tipo": "", "mensaje": ""}

    try:
        usuario_interno = list(mongo.db.usuarios.find({'nombre_usuario': nombre_usuario}))
        if len(usuario_interno) == 0:
            mensaje["tipo"] = "credenciales_erroneas"
            mensaje["mensaje"] = "Credenciales erroneas"
            return jsonify(mensaje)
        else:
            contrasena_md5hash = hashlib.md5(contrasena.encode())

            if contrasena_md5hash.hexdigest() == usuario_interno[0]['contrasena']:
                mensaje_entrada = {
                    'tipo': 'aprobado',
                    'mensaje': {
                        'tipo': usuario_interno[0]['tipo'],
                        'documento': usuario_interno[0]['documento']
                    }
                }
                return jsonify(mensaje_entrada)
            else:
                mensaje["tipo"] = "credenciales_erroneas"
                mensaje["mensaje"] = "Credenciales erroneas"
                return jsonify(mensaje)

    except Exception as exception:
        print("==========LOGIN=========")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)
    
