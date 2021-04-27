'''Escribir un programa que pida al usuario una palabra y muestre
por pantalla si es un palíndromo.'''

import argparse


def operation():
    word = args.word.lower().replace(" ", "")
    if word == word[::-1]:
        print("La palabra ({}) es un palíndromo.".format(args.word))
    else:
        print("La palabra ({}) NO es un palíndromo.".format(args.word))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", help="Palabra a analizar", type=str, required=True)
    args = parser.parse_args()
    operation()
