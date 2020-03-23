from project import mongo

def validar_documento(documento):
    try: 
        usuario = list(mongo.db.usuarios.find({'documento': documento}))
        if len(usuario[0]) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======DOC_EXS======")
        print(exception)
        return False


def validar_usuario(usuario):
    try: 
        usuario_db = list(mongo.db.usuarios.find({'usuario': usuario}))
        if len(usuario_db[0]) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======USE_EXS======")
        print(exception)
        return False

    
def validar_correo(correo):
    try: 
        usuario = list(mongo.db.usuarios.find({'correo': correo}))
        if len(usuario[0]) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("=====MAIL_EXS======")
        print(exception)
        return False