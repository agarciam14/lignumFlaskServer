from flask import jsonify
from flask import request
from flask import Blueprint
import json
import urllib.request as urllib
from project import mongo

ranking_app = Blueprint("ranking_app", __name__)

@ranking_app.route('/api/ranking/traer_ranking', methods=['GET'])
def traer_ranking():
    try:
        mensaje = {"tipo": "", "mensaje": ""}

        ranking = list(mongo.db.usuarios.find({}).sort("puntos",-1))
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = ranking

        return jsonify(mensaje)
    except Exception as exception:
        print("======RANKING=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

