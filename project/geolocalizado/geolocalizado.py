from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo

geolocalizador_app = Blueprint("geolocalizador_app", __name__)

# Este metodo es solo una muestra de como se comienza a usar Flask y sus
# peticiones pero este metodo no pertenece a backend
@geolocalizador_app.route('/api/geolocalizado/test_get', methods=['GET'])
def test_get():
    try:
        user = request.args['user']
        edad = request.args['edad']
        print(user)
        return jsonify({message: 'pase'})
    except Exception as excepciond:
        print("No se logro hacer metodo get")
        print(exception)
        return jsonify({message: 'no pase'})

    
@geolocalizador_app.route('/api/geolocalizado/test_post')
def test_post():
    try:
        correo = request.json['correo']
        llave = request.json['llave']
        print(correo)
        return jsonify(True)
    except Exception as exception:
        print("NO se logro hacer metodo post")
        print(exception)
        return jsonify(False)
    
