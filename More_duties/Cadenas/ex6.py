'''Escribir un programa que pida al usuario que introduzca una frase en la
consola y una vocal, y después muestre por pantalla la misma frase
pero con la vocal introducida en mayúscula.'''

import argparse
import re


def operation():
    vowels = ["a", "e", "i", "o", "u"]
    if(args.vowel in args.text):
        vowel_mayus = re.sub(args.vowel, args.vowel.upper(), args.text)
        print(vowel_mayus)
    elif(args.vowel not in (letter.upper() for letter in vowels) or args.vowel not in vowels):
        print("El elemento {} no es un vocal.".format(args.vowel))
    else:
        print("La vocal {} no existe en la frase ({}).".format(args.vowel, args.text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", type=str, help="Frase para analizar", required=True)
    parser.add_argument("-v", "--vowel", type=str, help="Vocal", required=True)
    args = parser.parse_args()
    operation()
