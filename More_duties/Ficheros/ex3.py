'''Escribir una función que pida dos números n y m entre 1 y 10, lea el
fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre
por pantalla la línea m del fichero. Si el fichero no existe debe mostrar
un mensaje por pantalla informando de ello.'''
import os
import argparse


def request():
    a = args.enteros[0]
    b = args.enteros[1]
    if os.path.exists("tabla-{}.txt".format(a)):
        print("Fichero tabla-{}.txt\n".format(a))
        with open("tabla-{}.txt".format(a), "r") as file:
            for x in file.readlines():
                if "{0} * {1}".format(a, b) in x:
                    print(x)
                    break
    else:
        print("El archivo tabla-{}.txt no existe".format(a))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('enteros', metavar='N', type=int, nargs='+',
                        help='valores enteros para el programa')
    args = parser.parse_args()
    request()
