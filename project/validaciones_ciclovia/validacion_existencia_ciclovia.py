from project import mongo

def validar_existencia_ciclovia(nombre):
    try:
        ciclovia = list(mongo.db.ciclovia.find({'nombre_ciclovia': nombre}))

        if len(ciclovia) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======CICLOVIA_EXS======")
        print(exception)
        return False
