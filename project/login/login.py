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
    contrasena = request.json['contrasena']

    mensaje = {"tipo": "", "mensaje": ""}

    try:
        usuario_interno = list(mongo.db.usuarios.find({'usuario': usuario}))
        if usuario_interno[0].len() == 0:
            mensaje["tipo"] = "credenciales_erroneas"
            mensaje["mensaje"] = "Credenciales erroneas"
            return jsonify(mensaje)
        else:
            contrasena_md5hash = hashlib.md5(contrasena.encode())
            if contrasena_md5hash == usuario_interno[0]['contrasena']:
                mensaje["tipo"] = usuario_interno[0]['tipo']
                mensaje["mensaje"] = "Aprobado"
                return jsonify(mensaje)
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
    
