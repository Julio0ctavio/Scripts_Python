'''Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje
"En <asignatura> has sacado <nota>." Todo esto con el uso de listas o tuplas.'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
boleta = []

for x in asignaturas:
    boleta.append(x + "=" + input("Ingrese su calificación para {} \n".format(x)))

for y in boleta:
    info = tuple(y.split("="))
    print("En {} has sacado {}".format(info[0], info[1]))
