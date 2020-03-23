import hashlib

def contrasena_md5(contrasena):
    md5_contrasena = ""
    md5_contrasena = hashlib.md5(contrasena.encode()).hexdigest()

    return md5_contrasena

def validacion_contrasena_segura(contrasena):
    return True
