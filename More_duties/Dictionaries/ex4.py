'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes>
es el nombre del mes.'''
import argparse
import locale
import calendar
import re


def operation():
    if(re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", args.fecha)):
        meses = {}
        for x in range(1, 13):
            if x < 10:
                y = "0" + str(x)
                meses[y] = calendar.month_name[x]
            else:
                meses[str(x)] = calendar.month_name[x]
        fecha = re.sub(r"/", "-", args.fecha)
        dia = re.search(r"^(\d{1,2})", fecha).group()
        mes = re.search(r"-(\d{1,2})-", fecha).group().strip("-")
        anio = re.search(r"(\d{4})", fecha).group()
        if(re.match(r"^\d$", dia)):
            dia = "0" + dia
        if(re.match(r"^\d$", mes)):
            mes = "0" + mes
        print("{} de {} del año {}".format(dia, meses[str(mes)], anio))
    else:
        print("Formato no válido para la fecha, el formato es: dd/mm/aaaa")


if __name__ == "__main__":
    # Para adaptar el idioma a español de México
    locale.setlocale(locale.LC_ALL, 'es-MX')
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fecha", type=str, help="Fecha de nacimiento",
                        required=True)
    args = parser.parse_args()
    operation()
