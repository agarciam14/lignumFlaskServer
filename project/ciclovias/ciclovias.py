from flask import jsonify
from flask import request
from flask import Blueprint
import json
import urllib.request as urllib

ciclovias_app = Blueprint("ciclovias_app", __name__)

@ciclovias_app.route('/api/ciclovias/traer_ciclovias', methods=['GET'])
def traer_ciclovias():
    try:
        mensaje = {"tipo": "", "mensaje": ""}

        usuarios = list(mongo.db.ciclovias.find({}))

        ciclovias_a_retornar = retirar_info_ciclovias(ciclovias)
        
        mensaje["tipo"] = 'aprobado'
        mensaje["mensaje"] = ciclovias_a_retornar

        return jsonify(mensaje)
    except Exception as exception:
        print("======USUARIOS=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la base de datos"
        return jsonify(mensaje)

def retirar_info_usuarios(ciclovias):
    usuarios_a_ciclovias = []
    for ciclo in ciclovias:
        ciclovia = {
            'nombre_ciclovia' : '',
            'dia': '',
            'hora_inicio': '',
            'hora_fin': '',
            'ruta': '',
        }
        ciclovia['nombre_ciclovia'] = ciclo['nombre_ciclovia']
        ciclovia['dia'] = ciclo['dia']
        ciclovia['hora_inicio'] = ciclo['hora_inicio']
        ciclovia['hora_fin'] = ciclo['hora_fin']
        ciclovia['ruta'] = ciclo['ruta']

        ciclovias_a_retornar.append(ciclovia)
    return ciclovias_a_retornar