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

        ranking = list(mongo.db.usuarios.find().sort("puntos",-1))
        ranking_seguro = retirar_ranking(ranking)
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = ranking_seguro

        return jsonify(mensaje)
    except Exception as exception:
        print("======RANKING=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

def retirar_ranking(ranking):
    ranking_a_retornar = []
    for rank in ranking:
        ranking = {
            "nombre_usuario" : "",
            "puntos" : ""
        }
        ranking["nombre_usuario"] = rank["nombre_usuario"]
        ranking["puntos"] = rank["puntos"]

        ranking_a_retornar.append(ranking)
    return ranking_a_retornar


