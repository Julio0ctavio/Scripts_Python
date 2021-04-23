'''Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas.'''

number = abs(int(input("Ingresa un numero entero positivo: \n")))
nopar = []
count = 1
while count <= number:
    nopar.append(count)
    count += 2
print("Numeros impares hasta el {}\n".format(number))
print(nopar)
