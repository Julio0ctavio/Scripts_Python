'''Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es una de las asignaturas de la lista.'''


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for x in asignaturas:
    print("Yo estudio {}, donde {} es una de las asignaturas de la lista."
          .format(x, x))
