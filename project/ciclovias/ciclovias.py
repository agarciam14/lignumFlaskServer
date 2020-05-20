from flask import jsonify
from flask import request
from flask import Blueprint
import json
import urllib.request as urllib
from project import mongo

ciclovias_app = Blueprint("ciclovias_app", __name__)

@ciclovias_app.route('/api/ciclovias/traer_ciclovias', methods=['GET'])
def traer_ciclovias():
    try:
        mensaje = {"tipo": "", "mensaje": ""}

        ciclovias = list(mongo.db.ciclovias.find({}))
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = ciclovias
        print(mensaje["mensaje"])

        return jsonify(mensaje)
    except Exception as exception:
        print("======CICLO-VIA=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

