'''Escribir un programa que pida al usuario un número entero positivo mayor
que 2 y muestre por pantalla si es un número primo o no.'''

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
