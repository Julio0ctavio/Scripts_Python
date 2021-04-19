'''Escribir un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con
la primera letra del nombre y de los apellidos en mayúscula.
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.'''

nombre_c = input("Ingrese su nombre completo: \n")

print(nombre_c.lower())
print(nombre_c.upper())

name_l = ""
name_s = nombre_c.split(" ")

for name in name_s:
    name_l = name_l + name.capitalize() + " "

print(name_l)
