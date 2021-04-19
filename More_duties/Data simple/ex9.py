'''Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''


inv = float(input("Cantidad a invertir: \n $ "))
int_a = float(input("Interés Anual: \n % "))
anios = float(input("Tiempo de ahorro en años: \n"))
ahorro = inv * ((int_a / 100) + 1) ** anios
print("Su ahorro es de : $ {:.2f}".format(ahorro))
