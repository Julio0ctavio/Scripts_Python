'''Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre
por pantalla ordenados de menor a mayor.'''

ganadores = input("Ingrese los numeros ganadores separados por coma (23,22,3,4): \n")
winners_num = ganadores.split(",")
# De mayor a menor: winners_num.sort(reverse=True)
# De menor a mayor:
winners_num.sort()
print(winners_num)
