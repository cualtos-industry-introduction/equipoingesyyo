from flask import Flask, render_template, request
from agenda import Agenda
from contacto import Contacto
from consultas import mostrar_contactos, consultar_contacto, agregar_contacto, actualizar_contacto,eliminar_contacto

app = Flask(__name__)




def mostrar_menu():
    print("Agenda")
    print("Selecciona la acción que desees efectuar")
    print("1. Agregar contactos")
    print("2. Mostar contactos")
    print("3. Consulta de contactos")
    print("4. Actualizar contactos")
    print("5. Eliminar contactos")
    print("6. Salir")

salida = "1"
"""while(salida == "1"):
    mostrar_menu()
    entrada = input ("Escribe la opcion: ")
    
    if entrada == "1":
        nuevo_contacto = Contacto(input("Ingresa el nombre: "))
        nuevo_contacto.empresa = input("Ingresa empresa: ")
        nuevo_contacto.correo = input("Ingresa correo: ")
        nuevo_contacto.telefono = input("Ingresa telefono: ")
        nuevo_contacto.nota = input("Ingresa nota: ")
        contactos.append(nuevo_contacto)
        agenda.agregarContactos(contactos)
        agenda.guardar()
        
    elif entrada == "2":
         print(agenda.mostrarContactos())
    elif entrada == "3":
         consulta = input ("Escriba el nombre a consultar ")
         print(agenda.obtenerContacto(consulta))
    elif entrada == "4":
         print("")
    elif entrada == "5":
         print("")
    elif entrada ==  "6":
        exit()
    else:
        print("Opcion no valida")"""

 #Hacer rutas   
     
@app.route('/')
def indice():
    return render_template ('indice.html')

@app.route('/mostrar_agenda')
def mostrar_agenda():
    agenda = Agenda('nueva_agenda')
    contactos = agenda.obtenerContactos()
    return render_template ('mostrar_contactos.html', contactos=contactos)

@app.route('/agregar_agenda', methods=['GET', 'POST'])
def agregar_agenda():
    agenda = Agenda('nueva_agenda')
    contactos = agenda.obtenerContactos()
    
    if request.method == 'POST':
        nuevo_contacto = Contacto(request.form['nombre'])        
        nuevo_contacto.empresa=request.form['empresa']
        nuevo_contacto.correo=request.form['correo']
        nuevo_contacto.telefono=request.form['telefono']
        nuevo_contacto.nota=request.form['nota']
        contactos.append(nuevo_contacto)
        agenda.agregarContactos(contactos)
        agenda.guardar()
        contacto = nuevo_contacto.obtenerDatos()
        agregar_contacto(contacto)
        return render_template('indice.html')
    elif request.method == 'GET':
        return render_template('agregar_agenda.html')

@app.route('/consultar_agenda',methods=['GET', 'POST'])

def consultar_agenda():
    if request.method == 'POST':
        consulta = consultar_contacto(request.form['nombre'])
        return render_template ('consultar_agenda.html', consulta=consulta)
    elif request.method == 'GET':
        consulta={}
        return render_template ('consultar_agenda.html',consulta=consulta)

@app.route('/actualizar_agenda')
def actualizar_agenda():
    return render_template ('actualizar_agenda.html')

@app.route('/eliminar_agenda')
 
def eliminar_agenda():
    if request.method == 'POST':
        consulta = eliminar_contacto(request.form['nombre'])
        return render_template ('eliminar_agenda.html', consulta=consulta)
        request.DeleteOne({'nombre': consulta})
    elif request.method == 'GET':
        consulta={}
        return render_template ('eliminar_agenda.html',consulta=consulta)

if __name__ == "__main__":
    app.run()