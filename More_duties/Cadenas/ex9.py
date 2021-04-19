'''Escribir un programa que pregunte al usuario la fecha de su nacimiento
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter.'''

import argparse
import locale
import re
from datetime import date


def operation():
    if(re.match(r"^(\d+)/(\d+)/(\d{4})$", args.fecha)):
        iso_format = re.sub(r"/", "-", args.fecha)
        iso_format_day = re.search(r"^(\d+)", iso_format).group()
        iso_format_month = re.search(r"-(\d+)-", iso_format).group().strip("-")
        iso_format_year = re.search(r"(\d{4})", iso_format).group()
        if(re.match(r"^\d$", iso_format_day)):
            iso_format_day = "0" + iso_format_day
        if(re.match(r"^\d$", iso_format_month)):
            iso_format_month = "0" + iso_format_month
        fecha = date.fromisoformat(iso_format_year + "-" + iso_format_month
                                   + "-" + iso_format_day)
        return fecha  # fecha
    else:
        print("Formato no válido para la fecha, el formato es: dd/mm/aaaa")
        return 0


def formating_date(fecha):
    return fecha.strftime("Fecha: %A %d de %B de %Y")


if __name__ == "__main__":
    # Para adaptar el idioma a español de México
    locale.setlocale(locale.LC_ALL, 'es-MX')
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fecha", type=str, help="Fecha de nacimiento",
                        required=True)
    args = parser.parse_args()
    fecha = operation()
    print(formating_date(fecha))
