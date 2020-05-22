from flask import jsonify
from flask import request
from flask import Blueprint
import json

from project.validaciones_usuario.validaciones_existencia_usuario import *
from project.validaciones_meta.validaciones_existencia_meta import *
from project.seguridad.seguridad import contrasena_md5
from project.seguridad.seguridad_contrasena import validacion_contrasena_segura
from project import mongo

crud_administrador_app = Blueprint("crud_administrador_app", __name__)

@crud_administrador_app.route('/api/crud_administrador/crear_usuario', methods=['POST'])
def crear_usuario():
    usuario = request.json['usuario']

    mensaje = {"tipo": "", "mensaje": ""}

    if validar_existencia_documento(usuario['documento']):
        if validar_existencia_correo(usuario['correo']):
            if validar_existencia_usuario(usuario['nombre_usuario']):
                if validacion_contrasena_segura(usuario['nombre_usuario'], usuario['contrasena']): 
                    try:

                        guardar_usuario_nuevo(usuario)

                        mensaje["tipo"] = "aprobado"
                        mensaje["mensaje"] = "Usuario creado con exito"
                        return jsonify(mensaje)
                    except Exception as exception:
                        print("======REG_U_NUEVO=====")
                        print(exception)
                        mensaje["tipo"] = "error_interno"
                        mensaje["mensaje"] = "Error en la conexion con la base de datos"
                        return jsonify(mensaje)
                else:
                    mensaje["tipo"] = "error_contrasena"
                    mensaje["mensaje"] = "La contrasena no cumple con las medidas de seguridad"
                    return jsonify(mensaje)
            else:
                mensaje["tipo"] = "error_nombre_usuario"
                mensaje["mensaje"] = "Nombre de usuario ya existe"
                return jsonify(mensaje)
        else:
            mensaje["tipo"] = "error_correo"
            mensaje["mensaje"] = "Correo ya registrado"
            return jsonify(mensaje)
    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "Documento ya registrado"
        return jsonify(mensaje)

def guardar_usuario_nuevo(usuario):
    contrasena_hash = contrasena_md5(usuario['contrasena'])
    usuario_a_guardar = {
        '_id': usuario['documento'],
        'nombre_usuario': usuario['nombre_usuario'],
        'documento': usuario['documento'],
        'correo': usuario['correo'],
        'contrasena': contrasena_hash,
        'imagen': usuario['imagen'],
        'tipo': usuario['tipo'],
        'puntos': 0,
        'arboles': [],
        'km_recorridos': 0,
        'dias_uso_cv': 0,
        'dias_uso_cr': 0,
        'tiempo_uso_cv': 0,
        'tiempo_uso_cr': 0,
        'tareas_realizadas': []
    }
    mongo.db.usuarios.insert_one(usuario_a_guardar)


@crud_administrador_app.route('/api/crud_administrador/modificar_usuario', methods=['POST'])
def modificar_usuario():
    usuario = request.json['usuario']

    mensaje = {"tipo": "", "mensaje": ""}
    print(usuario)
    if validar_existencia_documento(usuario['documento']) == False:
        if validar_existencia_correo_modificar(usuario['documento'], usuario['correo']):
            if validar_existencia_usuario_modificar(usuario['documento'], usuario['nombre_usuario']):
                try:

                    mongo.db.usuarios.update({'_id': usuario['documento']}, {'$set': {'nombre_usuario': usuario['nombre_usuario'], 'correo': usuario['correo'], 'imagen': usuario['imagen']}})

                    mensaje["tipo"] = "aprobado"
                    mensaje["mensaje"] = "Usuario modificado con exito"
                    return jsonify(mensaje)
                except Exception as exception:
                    print("======MOD_USUA=====")
                    print(exception)
                    mensaje["tipo"] = "error_interno"
                    mensaje["mensaje"] = "Error en la conexion con la base de datos"
                    return jsonify(mensaje)
            else:
                mensaje["tipo"] = "error_nombre_usuario"
                mensaje["mensaje"] = "Nombre de usuario ya existe"
                return jsonify(mensaje)
        else:
            mensaje["tipo"] = "error_correo"
            mensaje["mensaje"] = "Correo ya registrado"
            return jsonify(mensaje)
    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuario no se encuentra registrado"
        return jsonify(mensaje)


@crud_administrador_app.route('/api/crud_administrador/modificar_contrasena', methods=['POST'])
def cambiar_contrasena():
    documento = request.json['documento']
    nombre_usuario = request.json['nombre_usuario']
    contrasena = request.json['contrasena']

    mensaje = {"tipo": "", "mensaje": ""}

    if validar_existencia_documento(documento) == False:
        if validacion_contrasena_segura(nombre_usuario, contrasena): 
            try:

                contrasena_hash = contrasena_md5(contrasena)

                mongo.db.usuarios.update({'_id': documento}, {'$set': {'contrasena': contrasena_hash}})

                mensaje["tipo"] = "aprobado"
                mensaje["mensaje"] = "Contrasena modificada con exito"
                return jsonify(mensaje)
            except Exception as exception:
                print("======MOD_CONTRA=====")
                print(exception)
                mensaje["tipo"] = "error_interno"
                mensaje["mensaje"] = "Error en la conexion con la base de datos"
                return jsonify(mensaje)
        else:
            mensaje["tipo"] = "error_contrasena"
            mensaje["mensaje"] = "La contrasena no cumple con las medidas de seguridad"
            return jsonify(mensaje)
    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuario no se encuentra registrado"
        return jsonify(mensaje)
        

@crud_administrador_app.route('/api/crud_administrador/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    usuario = request.json['usuario']

    mensaje = {"tipo": "", "mensaje": ""}
    # El se puede eliminar a el mismo?
    # Que pasa si solo queda un usuario y se elimina?
    if validar_existencia_documento(usuario['documento']) == False:
        try:

            mongo.db.usuarios.remove({'_id': usuario['documento']})

            mensaje["tipo"] = "aprobado"
            mensaje["mensaje"] = "Usuario eliminado con exito"
            return jsonify(mensaje)
        except Exception as exception:
            print("======ELI_USUA=====")
            print(exception)
            mensaje["tipo"] = "error_interno"
            mensaje["mensaje"] = "Error en la conexion con la base de datos"
            return jsonify(mensaje)

    else:
        mensaje["tipo"] = "error_documento"
        mensaje["mensaje"] = "El usuaio no se encuentra registrado"
        return jsonify(mensaje)


@crud_administrador_app.route('/api/crud_administrador/crear_meta', methods=['POST'])
def crear_meta():
    meta = request.json['meta']

    mensaje = {"tipo": "", "mensaje": ""}

    if validar_existencia_meta(meta['nombre_meta']):
        try:
            guardar_meta_nueva(meta)

            mensaje["tipo"] = "aprobado"
            mensaje["mensaje"] = "Meta creada con exito"
            return jsonify(mensaje)
        except Exception as exception:
            print("======REG_META_NUEVA=====")
            print(exception)
            mensaje["tipo"] = "error_interno"
            mensaje["mensaje"] = "Error en la conexion con la base de datos"
            return jsonify(mensaje)
                
    else:
        mensaje["tipo"] = "error_nombre_meta"
        mensaje["mensaje"] = "Meta ya registrada"
        return jsonify(mensaje)

def guardar_meta_nueva(meta):
    meta_a_guardar = {
        '_id' : meta['nombre_meta'],
        'nombre_meta' : meta['nombre_meta'],
        'objetivo' : meta['objetivo'],
        'descripcion' : meta['descripcion'],
        'puntaje' : meta['puntaje'],
        'dependencias' : meta['dependencias']
    }
    mongo.db.metas.insert_one(meta_a_guardar)
    print(meta_a_guardar)
    