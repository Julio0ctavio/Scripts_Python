'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número
de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.'''

import re
import argparse


def operation():
    tel_format = re.match(r"^\+(\d{2})-(\d+)-(\d{2})$", args.telephone)
    if tel_format:
        find_tel = re.search(r"-(\d+)-", args.telephone).group()
        print("N° de telefono filtrado: ", find_tel.strip("-"))
    else:
        print("Ingrese un formato valido: +##-########-##")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--telephone", help="teléfono completo", type=str, required=True)
    args = parser.parse_args()
    operation()
