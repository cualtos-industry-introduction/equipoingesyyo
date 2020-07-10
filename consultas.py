from pymongo import MongoClient, DeleteOne

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
    resultado = coleccion.find_one({'nombre': titulo})
    return resultado

def agregar_contacto(registros):
    id = coleccion.insert_one(registros)
    return id

def actualizar_contacto(nombre, registros):
    resultado = coleccion.update_one({'nombre': nombre}, 
        {'$set': {'correo': registros['correo']}})
    return str(resultado.modified_count)

    