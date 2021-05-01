'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
y muestre su símbolo o un mensaje de aviso si la divisa no está
en el diccionario.'''
import argparse


def operation():
    divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    if args.moneda in divisas.keys():
        print("{} -> {}".format(args.moneda, divisas[args.moneda]))
    else:
        print("La divisa ({}) no está disponible.".format(args.moneda))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--moneda", help="Divisa para analizar.",
                        type=str, required=True)
    args = parser.parse_args()
    operation()
