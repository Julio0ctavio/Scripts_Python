'''Escribir un programa que almacene en una lista los siguientes precios
, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor
de los precios.'''

prices = [50, 75, 46, 22, 80, 65, 8]
prices.sort()

print("Precio menor: $ {:,} | Precio mayor: $ {:,}"
      .format(prices[0], prices[len(prices)-1]))
