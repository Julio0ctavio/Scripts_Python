'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada
un nuevo dato debe imprimirse el contenido del diccionario.'''

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    # Nueva forma de asignar un booleano. "a = input("Si o No") == "Si"
    # donde Si es igual a True"
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
