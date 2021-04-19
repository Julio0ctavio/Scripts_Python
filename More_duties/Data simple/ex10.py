'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en
el último pedido y calcule el peso total del paquete que será enviado.'''

import argparse


def operation():
    payaso = 112
    muneca = 75
    peso_total = "{:,}".format((args.payaso*payaso + muneca*args.muneca) / 1000)
    peso_payaso = "{:,}".format((args.payaso*payaso) / 1000)
    peso_muneca = "{:,}".format((muneca*args.muneca) / 1000)
    print("Estadísticas: \n Peso muñecas: {} Kg || Peso payasos {} Kg ::\n Peso Total {} Kg".format(
        peso_muneca, peso_payaso, peso_total))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--payaso', help='Cantidad de payasos', required=True, type=int)
    parser.add_argument('-m', '--muneca', help='Cantidad de muñecas', required=True, type=int)
    args = parser.parse_args()
    operation()
