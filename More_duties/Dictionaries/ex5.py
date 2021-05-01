'''Escribir un programa que almacene el diccionario con los créditos de las
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
después muestre por pantalla los créditos de cada asignatura en el formato
<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
también el número total de créditos del curso.'''

dyc = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for x, y in dyc.items():
    print("{0} tiene {1} crédito(s), donde {0} es cada una de las asignaturas del curso, y {1} son sus créditos."
          .format(x, y))
    total += y
print("Total de créditos por este curso {}".format(total))
