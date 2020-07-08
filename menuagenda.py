from flask import Flask, render_template
from agenda import Agenda
from contacto import Contacto

app = Flask(__name__)


agenda = Agenda('nueva_agenda')
contactos = agenda.obtenerContactos()

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


if __name__ == "__main__":
    app.run()