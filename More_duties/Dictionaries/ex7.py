'''Escribir un programa que cree un diccionario simulando una cesta de la
compra. El programa debe preguntar el artículo y su precio y añadir el par
al diccionario, hasta que el usuario decida terminar. Después se debe mostrar
por pantalla la lista de la compra y el coste total, con el siguiente formato'''

cesta = {}
cierre = True
total = 0

while cierre:
    key = input("Ingrese el artículo: \n")
    value = int(input("Precio para {}: $".format(key)))
    cesta[key] = value
    total += value
    cierre = input("¿Desea continuar agregando artículos? y/n: ") == "y"

print("Lista de Compra")
for x, y in cesta.items():
    print("{}\t$ {:,}".format(x, y))
print("Total\t$ {:,}".format(total))
