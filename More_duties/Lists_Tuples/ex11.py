'''Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.'''

A = [1, 2, 3]
B = [-1, 0, 2]
C = []
resultado = 0
for x in range(0, 3):
    C.append(A[x]*B[x])
    resultado = resultado + C[x]

print("Prodcuto Escalar de A * B -> C {} = {}".format(C, resultado))
