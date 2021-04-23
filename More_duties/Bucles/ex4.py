'''Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla la cuenta atrás desde ese número hasta
cero separados por comas.'''

number = abs(int(input("Ingrese un numero entero positivo: \n")))
count = 0 - number
neg_n = []
while count <= 0:
    neg_n.append(count)
    count += 1
print(neg_n)
