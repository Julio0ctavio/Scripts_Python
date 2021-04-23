'''Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida
empezando por la última.'''
import argparse


def operation():
    for x in args.word[::-1]:
        print(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", type=str, required=True,
                        help="Palabra para recorrer al reves")
    args = parser.parse_args()
    operation()
