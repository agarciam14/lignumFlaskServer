from project import mongo

def validar_existencia_meta(nombre):
    try: 
        meta_db = list(mongo.db.metas.find({'nombre_meta': nombre}))

        if len(meta_db) == 0:
            return True
        else:
            return False
    
    except Exception as exception:
        print("======META_EXS======")
        print(exception)
        return False

    