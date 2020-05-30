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

        ciclovias_a_retornar = retirar_info_ciclovias(ciclovias)
        
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = ciclovias_a_retornar
        print(mensaje["mensaje"])

        return jsonify(mensaje)
    except Exception as exception:
        print("======CICLO-VIA=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

def retirar_info_ciclovias(ciclovias):
    ciclovias_a_retornar = []
    for ciclo in ciclovias:
        ciclovia = {
            'nombre_ciclovia' : '',
            'hora_inicio': '',
            'hora_fin': '',
            'ruta': {
                'inicio': {
                    'lat': '',
                    'log': ''
                },
                'fin': {
                    'lat': '',
                    'log': ''
                }
            },
            'dia': '',
        }
        ciclovia = ciclo
        print(ciclovia)
        ciclovias_a_retornar.append(ciclovia)
    return ciclovias_a_retornar