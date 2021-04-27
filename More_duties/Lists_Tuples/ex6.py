'''Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine
de la lista las asignaturas aprobadas (menor a 7). Al final el programa debe mostrar
por pantalla las asignaturas que el usuario tiene que repetir.
Todo esto con el uso de listas o tuplas.'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
boleta = []

for x in asignaturas:
    boleta.append(x + "=" + input("Ingrese su calificación para {} \n".format(x)))

for x in boleta:
    info = tuple(x.split("="))
    if(int(info[1]) >= 7):
        asignaturas.remove(info[0])

if(len(asignaturas) == 0):
    print("Buen trabajo, usted no tiene asignaturas reprobadas.")
else:
    print("Lamentablemente, debe aprobar las siguientes asignaturas: {}"
          .format(asignaturas))
