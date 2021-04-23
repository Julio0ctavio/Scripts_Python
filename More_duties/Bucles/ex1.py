'''Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces.'''
import argparse


def operation():
    count = 0
    while count < 10:
        print(args.word)
        count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", type=str,
                        help="Word to show inside the bucle",
                        default=None, required=True)
    args = parser.parse_args()
    operation()
