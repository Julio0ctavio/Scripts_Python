'''Escribir una función que pida un número entero entre 1 y 10, lea el
fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es
el número introducido, y la muestre por pantalla. Si el fichero no existe
debe mostrar un mensaje por pantalla informando de ello.'''
import os


def request():
    n = int(input("Ingrese un número entero (1-10): "))
    if os.path.isfile("tabla-{}.txt".format(n)):
        file = open("tabla-{}.txt".format(n), "r")
        print(file.read())
    else:
        print("El archivo tabla-{}.txt no existe ...".format(n))


request()
