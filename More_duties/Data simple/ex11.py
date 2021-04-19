''' Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran
hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en
la cuenta de ahorros, introducida por el usuario. Después el programa debe
calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
segundo y tercer años. Redondear cada cantidad a dos decimales.'''

ahorro = float(input("Ingrese su cantidad a la cuenta de ahorro: \n $ "))
interes_anual = 0.04
balance1 = ahorro * (1 + interes_anual)
print("Balance tras el primer año: $ {:,}".format(round(balance1, 2)))
balance2 = balance1 * (1 + interes_anual)
print("Balance tras el segundo año: $ {:,}".format(round(balance2, 2)))
balance3 = balance2 * (1 + interes_anual)
print("Balance tras el tercer año: $ {:,}".format(round(balance3, 2)))
