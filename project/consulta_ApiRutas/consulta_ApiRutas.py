from flask import jsonify
from flask import request
from flask import Blueprint
import json
import urllib.request as urllib

consulta_ApiRutas_app = Blueprint("consulta_ApiRutas_app", __name__)

@consulta_ApiRutas_app.route('/api/consulta_ApiRutas/obtener_ruta', methods=['GET'])
def obtener_ruta():
    mensaje = {"tipo": "", "mensaje": ""}
    try:
        file_geo = urllib.urlopen("https://www.medellin.gov.co/mapas/rest/services/ServiciosPlaneacion/POT48_Sistema_colectivo/MapServer/14/query?where=1%3D1&outFields=*&outSR=4326&f=json")
        content = file_geo.read()
        json_file = json.loads(content)
        rutas_a_retornar = {"mensaje" : definicion_rutas(json_file)}
        return jsonify(rutas_a_retornar)
    except Exception as exception:
        print("======RUTAS=====")
        print(exception)
        mensaje["tipo"] = "error_interno"
        mensaje["mensaje"] = "Error en la conexion con la API rutas"
        return jsonify(mensaje)

def definicion_rutas(json_file):

    rutas = []

    for r in json_file["features"]:
        Nombre = r["attributes"]["NOMBRE"]
        ruta = {
            "Nombre": Nombre,
            "Path": r["geometry"]["paths"][0]
        }
        rutas.append(ruta) 

    return rutas



