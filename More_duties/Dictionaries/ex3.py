'''Escribir un programa que guarde en un diccionario los precios de las
frutas de la tabla, pregunte al usuario por una fruta, un número de kilos
y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.'''
import argparse


def operation():

    frutas = {
        "Platano": 1.35,
        "Manzana": 0.80,
        "Pera":	0.85,
        "Naranja": 0.70
    }

    if args.fruit in frutas.keys():
        print("\n{} a $ {} el Kg ==> {:.2f} Kg de {} igual a ${:.2f}"
              .format(args.fruit, frutas[args.fruit], args.quantity,
                      args.fruit, frutas[args.fruit]*args.quantity))
    else:
        print("La fruta {} no está disponible".format(args.fruit))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fruit", help="Fruta escogida.",
                        type=str, required=True)
    parser.add_argument("-q", "--quantity", help="Unidades.",
                        required=True, type=float)
    args = parser.parse_args()
    operation()
