'''Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el
capital obtenido en la inversión cada año que dura la inversión.'''

inv = float(input("Ingrese la cantidad a invertir: (Cantidad con o sin centavos) \n"))
interes = float(input("Cual es su interes anual? (Porcentaje entero %) \n"))
anios = int(input("Cuantos anios? \n"))
ganancia = 0
for x in range(1, anios):
    ganancia += (inv*interes)/100
    print("Capital obtenido para el anio {:.0f}: $ {:,}".format(x, ganancia))
