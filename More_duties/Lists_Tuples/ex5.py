'''Escribir un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.'''

num = list(range(1, 11))

for x in num[::-1]:
    if(x != 1):
        print(str(x) + ",", end=" ")
    else:
        print(str(x), end=" ")

print("\nTipo de dato: " + str(type(num)))
