'''Escribir un programa para gestionar un directorio telefónico con los nombres
y los teléfonos de los clientes de una empresa. El programa debe incorporar
funciones para crear el fichero con el directorio si no existe, para consultar el
teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar
el teléfono de un cliente.
El directorio debe estar guardado en el fichero de texto directorio.txt donde el
nombre del cliente y su teléfono deben aparecer separados por comas y
cada cliente en una línea distinta.'''
import time
import os


directorio = {}
cierre = True
id = 0


def status_dir():
    if(os.path.exists("directorio.txt") is False):
        open("directorio.txt", "a")
        print("Directorio creado con éxito!")
    else:
        print("Entrando al directorio ...")


while cierre:
    print("Directorio Telefónico de X Company S.A. \n")
    print("Ingrese la opción deseada: ")
    print("(1) Agregar un cliente al directorio\n(2) Eliminar teléfono de cliente\n(3) Mostrar teléfono de cliente\n" +
          "(4) Terminar.\n\n")
    x = int(input("Opción: "))
    if(x == 1):
        status_dir()
        nombre = input("Ingrese el nombre del cliente: ")
        tel = input("Ingrese su teléfono: ")
        file = open("directorio.txt", "a")
        file.write("{},{}\n".format(nombre, tel))
        file.close()
        file = open("directorio.txt", "r")
        order = sorted(file.readlines())
        file.close()
        os.remove("directorio.txt")
        new_file = open("directorio.txt", "a")
        for line in order:
            new_file.write(line)
        new_file.close()
        print("Cliente agregado al directorio -> {},{}".format(nombre, tel))

    elif(x == 2):
        status_dir()
        nombre = input("Ingrese el nombre del cliente: ")
        new_lines = []
        with open("directorio.txt", "r") as file:
            for line in file:
                if nombre in line:
                    new_lines.append("{},NA\n".format(nombre))
                else:
                    new_lines.append(line)
        sorted(new_lines)
        os.remove("directorio.txt")
        new_file = open("directorio.txt", "a")
        for line in new_lines:
            new_file.write(line)
        new_file.close()
        print("El número del cliente {} ha sido eliminado".format(nombre))

    elif(x == 3):
        status_dir()
        nombre = input("Ingrese el nombre del cliente: ")
        file = open("directorio.txt", "r")
        if nombre in file.read():
            file = open("directorio.txt", "r")
            for line in file.readlines():
                if nombre in line:
                    print(line)
                    break
            file.close()
        else:
            print("No existe el contacto {} en el dirctorio.".format(nombre))
        file.close()

    else:
        cierre = False
    time.sleep(4)
    os.system("cls")
