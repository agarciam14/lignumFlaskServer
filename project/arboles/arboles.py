from flask import jsonify
from flask import request
from flask import Blueprint
import json
import urllib.request as urllib
from project import mongo

arboles_app = Blueprint("arboles_app", __name__)

@arboles_app.route('/api/arboles/traer_arboles', methods=['GET'])
def traer_arboles():
    try:
        mensaje = {"tipo": "", "mensaje": ""}

        arboles = list(mongo.db.arboles.find())
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = arboles

        return jsonify(mensaje)
    except Exception as exception:
        print("======arboles=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)