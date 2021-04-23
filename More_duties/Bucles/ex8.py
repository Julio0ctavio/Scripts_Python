'''Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
altura = int(input("Ingrese el número para la base: \n"))
print("\nTriangulo de Valores Impar: \n")
nopar = 1
for x in range(1, altura+1):
    if x == 1:
        print(x)
    else:
        nopar += 2
        for y in range(nopar, 0, -2):
            print(y, end=" ")
        print("")
