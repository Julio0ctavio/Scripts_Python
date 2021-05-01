'''Escribir un programa que permita gestionar la base de datos de clientes de
una empresa. Los clientes se guardarán en un diccionario en el que la clave de
cada cliente será su ID, y el valor será otro diccionario con los datos del
cliente (nombre, dirección, teléfono, correo, preferente), donde preferente
tendrá el valor True si se trata de un cliente preferente.

El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
(4) Listar todos los clientes, (5) Listar clientes preferentes,
(6) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y
añadirlo a la base de datos.
Preguntar por el ID del cliente y eliminar sus datos de la base de datos.
Preguntar por el ID del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su ID y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF
y nombre.
Terminar el programa.

'''
import os
import time

clientes = {}
cierre = True
id = 0

while cierre:
    print("Sistema de Manejo de Clientes de X Company S.A. \n")
    print("Ingrese la opción deseada: ")
    print("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n" +
          "(4) Listar todos los clientes\n(5) Listar clientes preferentes\n" +
          "(6) Terminar.\n\n")
    x = int(input("Opción: "))
    if(x == 1):
        id += 1
        cliente = {}
        cliente["Nombre"] = input("Nombre: ")
        cliente["Dirección"] = input("Dirección: ")
        cliente["Teléfono"] = input("Teléfono: ")
        cliente["Correo"] = input("Correo: ")
        cliente["Pref"] = input("¿Es preferente? (Si/No) :")
        clientes[id] = cliente
        print("El cliente N°{} se ha dado de alta en el sistema.".format(id))
    elif(x == 2):
        id = int(input("Ingrese el ID del cliente: "))
        del(clientes[id])
        print("El cliente N°{} se ha dado de baja en el sistema.".format(id))
    elif(x == 3):
        id = int(input("Ingrese el ID del cliente: "))
        if id in clientes.keys():
            print("Cliente N°{}: \n".format(id))
            for x, y in clientes[id].items():
                print("{}: {}".format(x, y))
        else:
            print("El ID {} no está registrado.".format(id))
    elif(x == 4):
        print("\nClientes Registrados: ")
        for x, y in clientes.items():
            print("\nCliente N°{} || Nombre: {}".format(x, y["Nombre"]))
    elif(x == 5):
        print("\nClientes Preferentes: ")
        for x, y in clientes.items():
            if y["Pref"] == "Si":
                print("Cliente N°{} || Nombre: {}".format(x, y["Nombre"]))
    else:
        cierre = False
    time.sleep(5)
    os.system("cls")
