'''Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.'''

import argparse


def operation():
    return "{0:.0f} entre {1:.0f} da un cociente {2:.0f} y un resto {3:.0f}".format((args.first), (args.second), ((args.first//args.second)), ((args.first % args.second)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--first', type=float, help='First number', required=True)
    parser.add_argument('-s', '--second', type=float, help='First number', required=True)
    args = parser.parse_args()
    result = operation()
    print(result)
