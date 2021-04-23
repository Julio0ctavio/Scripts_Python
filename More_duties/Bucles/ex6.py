'''Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.'''

altura = int(input("Ingrese la altura del triángulo rectángulo: \n"))
for x in range(altura):
    print("*"*(x+1))
