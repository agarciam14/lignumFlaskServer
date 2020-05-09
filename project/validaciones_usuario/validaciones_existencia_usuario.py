from project import mongo

def validar_existencia_documento(documento):
    try:
        usuario = list(mongo.db.usuarios.find({'documento': documento}))

        if len(usuario) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======DOC_EXS======")
        print(exception)
        return False


def validar_existencia_usuario(usuario):
    try: 
        usuario_db = list(mongo.db.usuarios.find({'nombre_usuario': usuario}))

        if len(usuario_db) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======USE_EXS======")
        print(exception)
        return False

    
def validar_existencia_correo(correo):
    try: 
        usuario = list(mongo.db.usuarios.find({'correo': correo}))
        if len(usuario) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("=====MAIL_EXS======")
        print(exception)
        return False


def validar_existencia_correo_modificar(documento, correo):
    try:

        usuario_reciente = list(mongo.db.usuarios.find({'_id': documento}))
        correo_existente = list(mongo.db.usuarios.find({'correo': correo}))
        
        if usuario_reciente[0]['correo'] == correo:
            return True
        elif len(correo_existente) == 0:
            return True
        else:
            return False

    except Exception as exception:
        print("====MAIL_EXS_MOD====")
        print(exception)
        return False


def validar_existencia_usuario_modificar(documento, usuario):
    try:

        usuario_reciente = list(mongo.db.usuarios.find({'_id': documento}))
        usuario_existente = list(mongo.db.usuarios.find({'nombre_usuario': usuario}))
        
        if usuario_reciente[0]['nombre_usuario'] == usuario:
            return True
        elif len(usuario_existente) == 0:
            return True
        else:
            return False

    except Exception as exception:
        print("====USU_EXS_MOD====")
        print(exception)
        return False