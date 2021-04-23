'''Escribir un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece
la letra en la frase.'''

import argparse
import re


def coincidences(parameter):
    coincidences = re.search(r"{}".format(parameter), args.text.lower())
    if coincidences:
        coin_number = 0
        if coincidences:
            for x in args.text.lower():
                if x == parameter:
                    coin_number += 1
        return coin_number
    else:
        return 0


def operation():
    if args.letter != " ":
        matches = coincidences(args.letter.lower())
        if matches > 0:
            print("La letra {} se ecuentra {} veces".format(args.letter, matches))
        else:
            print("La letra {} NO ecuentra en la oracion: \n{}".format(args.letter, args.text))
    else:
        matches = coincidences(args.letter)
        if matches > 0 and matches == 1:
            print("Hay {} espacio en la oración".format(matches))
        elif(matches > 0):
            print("Hay {} espacios en la oración".format(matches))
        else:
            print("No hay espacios ...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", help="Texto para analisis",
                        required=True, type=str)
    parser.add_argument("-l", "--letter",
                        help="Letra elegida para el analisis",
                        required=True, type=str, default=None)
    args = parser.parse_args()
    operation()
