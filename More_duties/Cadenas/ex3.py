'''Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de
letras que tienen el nombre.'''

import argparse


def operation():
    print("'{0}' tiene ({1}) letras".format(args.name, len(args.name)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Nombre", required=True, type=str, default=None)
    args = parser.parse_args()
    operation()
