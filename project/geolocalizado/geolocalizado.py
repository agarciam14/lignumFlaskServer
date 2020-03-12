from flask import jsonify
from flask import request
from flask import Blueprint
import json

geolocalizador_app = Blueprint("geolocalizador_app", __name__)

# Este metodo es solo una muestra de como se comienza a usar Flask y sus
# peticiones pero este metodo no pertenece a backend
@geolocalizador_app.route('/api/geolocalizado/activar_ubicacion', methods=['GET'])
def activar_ubicacion():
    try:
        return jsonify(True)
    except Exception as excepcion:
        print("No se logro verificar si la ubicacion esta activada")
        return jsonify(False)
