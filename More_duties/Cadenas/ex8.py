'''Escribir un programa que pregunte por consola el precio de un producto en
pesos con dos decimales y muestre por pantalla el número de pesos
y el número de centavos del precio introducido.'''

import re

total = str(input("Ingrese el total: \n"))
total_centavos = (re.search(r"\.(\d{2})", total).group()).lstrip(".")
total_int = int(round(float(total), 0))
print("Total = $ {:,} pesos con {} centavos".format(total_int, total_centavos))
