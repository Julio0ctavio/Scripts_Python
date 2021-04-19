''' Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
calculado redondeado con dos decimales.'''

import argparse


def execute_action():
    total = args.weight / (args.length**2)
    status = ""
    if(total > 18.5):
        if(18.5 <= total <= 24.9):
            status = "normalidad"
        elif(25 <= total <= 29.9):
            status = "sobrepeso"
        elif(total >= 30):
            status = "obesidad"
    else:
        status = "bajo peso"
    return "{:.2f} (Kg/m2) con un estatus de {}".format(total, status)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-wg', '--weight', type=float,
                        help='weight in Kg', default=None, required=True)
    parser.add_argument('-lg', '--length', type=float, help='Lenght in meters (m)',
                        default=None, required=True)
    args = parser.parse_args()
    print("IMC ->  " + str(execute_action()))
