from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project import mongo
from project.validaciones_usuario.validaciones_existencia_usuario import validar_existencia_documento
from math import radians, cos, sin, asin, sqrt

usuario_general_app = Blueprint("usuario_general_app", __name__)

@usuario_general_app.route('/api/usuario_general/traer_datos_usuario', methods=['GET'])
def traer_datos_usuario():
    documento = request.args['documento']

    mensaje = {"tipo": "", "mensaje": ""}
    if validar_existencia_documento(documento) == False:
        try:
            datos_usuario = list(mongo.db.usuarios.find({'documento': documento}))[0]
            datos_usuario_limpio = retirar_datos_usuario(datos_usuario)

            mensaje["tipo"] = "aprobado"
            mensaje["mensaje"] = datos_usuario_limpio
            return jsonify(mensaje)
        except Exception as exception:
            print("======DATOS_USUA_GENERAL=====")
            print(exception)
            mensaje["tipo"] = "error_interno"
            mensaje["mensaje"] = "Error en la conexion con la base de datos"
            return jsonify(mensaje)

    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuaio no se encuentra registrado"
        return jsonify(mensaje)

def retirar_datos_usuario(datos_usuario):
    usuario = {
        'nombre_usuario': datos_usuario['nombre_usuario'],
        'documento': datos_usuario['documento'],
        'puntaje': datos_usuario['puntos'],
        'recorrido': datos_usuario['km_recorridos']
    }
    return usuario

@usuario_general_app.route('/api/usuario_general/modificar_recorrido', methods=['POST'])
def modificar_recorrido():
    usuario = request.json['usuario']
    puntos = request.json['puntos']
    print(usuario)
    mensaje = {"tipo": "", "mensaje": ""}
    if validar_existencia_documento(usuario['documento']) == False:
        try:
            recorrido = usuario['recorrido']
            for i in range (1,len(puntos)):
                prev_location = puntos[i-1]
                curr_location = puntos[i]
                recorrido+=haversine(prev_location,curr_location)

            mongo.db.usuarios.update({'_id': usuario['documento']}, {'$set': {'km_recorridos': recorrido}})
            mensaje["tipo"] = "aprobado"
            mensaje["mensaje"] = "Recorrido actualizado con exito"
            return jsonify(mensaje)
        except Exception as exception:
            print("======MOD_PUNTAJE=====")
            print(exception)
            mensaje["tipo"] = "error_interno"
            mensaje["mensaje"] = "Error en la conexion con la base de datos"
            return jsonify(mensaje)
            
    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuario no se encuentra registrado"
        return jsonify(mensaje)

def haversine(puntoA,puntoB):
    print(puntoA)
    lat1 = puntoA['lat']
    lon1 = puntoA['long']
    lat2 = puntoB['lat']
    lon2 = puntoB['long']
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r