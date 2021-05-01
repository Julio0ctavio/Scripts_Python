'''Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número
de teléfono es <teléfono>.'''

usuario = {}

usuario["Nombre"] = (input("Nombre: \n"))
usuario["Edad"] = input("Edad: \n")
usuario["Direccion"] = input("Direccion: \n")
usuario["Telefono"] = input("Telefono: \n")

print("\n\n{} tiene {} años, \n vive en {} \n y su número de de teléfono es {}"
      .format(usuario["Nombre"], usuario["Edad"], usuario["Direccion"],
              usuario["Telefono"]))
