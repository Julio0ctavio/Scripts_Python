'''Escribir un programa que muestre por pantalla la tabla de multiplicar
del 1 al 10.'''

for a in range(1, 11):
    for b in range(1, 11):
        print(a*b, end="\t")
    print("")
