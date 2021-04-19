'''Una panadería vende barras de pan a 3.49$ cada una.
El pan que no es el día tiene un descuento del 60%. Escribir un programa que
comience leyendo el número de barras vendidas que no son del día (merma).
Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.'''

merma = float(input("Ingrese la cantidad de merma: \n"))
precio_normal = 3.49
desc_merma = 0.6

print("Para pan fresco original -> $ {:,} \n Más descuento de 60% por merma -> {:,} \n Total -> $ {:,}".format(
    round(merma*precio_normal, 2), round(merma*precio_normal*desc_merma, 2), round(merma*precio_normal*(1-desc_merma), 2)))
