from pymongo import MongoClient, DeleteOne, ReplaceOne

cliente = MongoClient('localhost', 27017)
#db = cliente.ejemplo_pymongo
#coleccion = db.prueba
db = cliente['agenda']
#db = cliente.ejemplo
coleccion = db.datos

def mostrar_contactos():
    cursor = coleccion.find()
    return list(cursor)

def consultar_contacto(titulo):
    resultado = coleccion.find_one({'nombre': titulo})
    return resultado

def eliminar_contacto(titulo):
    resultado= coleccion.delete_one({'nombre': titulo})
    return resultado.deleted_count

def agregar_contacto(registros):
    id = coleccion.insert_one(registros)
    return id

def actualizar_contacto(nombre, registros):
    resultado = coleccion.update_one({'nombre': nombre}, 
        {'$set': {'empresa': registros['empresa'],'correo':registros['correo'],'telefono':registros['telefono'],'puesto':registros['puesto'],'nota':registros['nota']}})

        
    return str(resultado.modified_count)

    