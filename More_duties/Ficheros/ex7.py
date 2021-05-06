'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del
IBEX35 con las siguientes columnas: Nombre (nombre de la empresa),
Final (precio de la acción al cierre de bolsa),
Maximo (precio máximo de la acción durante la jornada),
Minimo (precio mínimo de la acción durante la jornada),
Volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y
devuelva un diccionario con los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto por la
función anterior y cree un fichero en formato csv con el mínimo,
el máximo y la media de dada columna.'''

import csv


def crear_dict(path):
    IBEX35 = {}
    index = 0
    headers = ()
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=";", quoting=csv.QUOTE_NONE)
        for row in reader:
            if index == 0:
                headers = row
            else:
                item = {}
                count = 0
                for col in headers:
                    item[col] = row[count]
                    count += 1
                IBEX35[index+1] = item
            index += 1
    return IBEX35


def crear_csv(dictionary):
    with open("nueva_cotizacion.csv", "w") as file:
        fieldnames = ["Minimo", "Maximo", "Medio"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for a, b in dictionary.items():
            maxi = float(b["Maximo"].replace(",", "."))
            mini = float(b["Minimo"].replace(",", "."))
            medio = (mini + maxi) / 2
            writer.writerow({"Minimo": "{:.2f}".format(maxi),
                             "Maximo": "{:.2f}".format(mini),
                             "Medio": "{:.2f}".format(medio)})


dict = crear_dict("cotizacion.csv")
crear_csv(dict)
