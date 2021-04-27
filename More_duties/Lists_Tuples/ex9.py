'''Escribir un programa que pida al usuario una palabra y
muestre por pantalla el número de veces que contiene cada vocal.'''

import argparse


def operation():
    word = args.word.lower().replace(" ", "")
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        count = 0
        for letter in word:
            if letter == vowel:
                count += 1
        print("Vocal {} aparece {} veces en ({})"
              .format(vowel, count, args.word))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", help="Palabra a analizar", type=str,
                        required=True)
    args = parser.parse_args()
    operation()
