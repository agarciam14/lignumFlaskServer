from project import mongo

def validar_existencia_ciclovia(nombre):
    try:
        ciclovia = list(mongo.db.ciclovia.find({'nombre_ciclovia': nombre}))

        if len(usuario) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======DOC_EXS======")
        print(exception)
        return False

