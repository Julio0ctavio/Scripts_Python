'''Escribir un programa que pregunte el nombre del
usuario en la consola y un número entero e imprima por
pantalla en líneas distintas el nombre del usuario tantas
veces como el número introducido.'''

import argparse


def operation():
    for i in range(0, abs(args.digit)):
        print(args.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="nombre", required=True)
    parser.add_argument("-d", "--digit", type=int, help="digito", required=True)
    args = parser.parse_args()
    operation()
