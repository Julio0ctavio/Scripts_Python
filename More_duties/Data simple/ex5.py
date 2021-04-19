'''Escribir un programa que pregunte al usuario por el
número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.'''

mport argparse


def execute_action():
    total = args.hours * args.value
    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-hrs', '--hours', type=int,
                        help='worked hours', default=None, required=True)
    parser.add_argument('-v', '--value', type=int, help='value per worked hour',
                        default=None, required=True)
    args = parser.parse_args()
    print("Total: $ " + str(execute_action()))
