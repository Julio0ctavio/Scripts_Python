'''El fichero calificaciones.csv contiene las calificaciones de un curso.
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de
prácticas.
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes
pudieron repetirlo al final del curso (convocatoria ordinaria).
Escribir un programa que contenga las siguientes funciones:

Una función que reciba el fichero de calificaciones y
devuelva una lista de diccionarios, donde cada diccionario contiene la
información de los exámenes y la asistencia de un alumno.
La lista tiene que estar ordenada por apellidos.

Una función que reciba una lista de diccionarios como la que devuelve la
función anterior y añada a cada diccionario un nuevo par con
la nota final del curso.
El peso de cada parcial de teoría en la nota final es de un 30% mientras
que el peso del examen de prácticas es de un 40%.

Una función que reciba una lista de diccionarios como la que devuelve
la función anterior y devuelva dos listas, una con los alumnos aprobados
y otra con los alumnos suspensos. Para aprobar el curso, la asistencia
tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales
y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.'''
import csv


def format_list(csvfile):
    lista_dict = []
    index = 0
    with open(csvfile, "r") as file:
        reader = csv.reader(file, delimiter=";", quoting=csv.QUOTE_NONE)
        headers = ()
        for x in reader:
            if index == 0:
                headers = x
            else:
                count_headers = 0
                usuario = {}
                for col in headers:
                    usuario[col] = x[count_headers]
                    count_headers += 1
                lista_dict.append(usuario)
            index += 1
    lista_dict.sort(key=lambda x: x.get("Apellidos"))  # Función discreta lambda
    return lista_dict


def examenes(usuario):

    if usuario["Parcial1"] != "":
        p1 = float(usuario["Parcial1"].replace(",", "."))
        # En caso de que haya presentado un examen ordinario
        if usuario["Ordinario1"] != "":
            p1o = float(usuario["Ordinario1"].replace(",", "."))
            if p1o != "" and p1o > p1:
                p1 = p1o
    elif usuario["Ordinario1"] != "":
        p1 = float(usuario["Ordinario1"].replace(",", "."))
    else:
        p1 = 0

    if usuario["Parcial2"] != "":
        p2 = float(usuario["Parcial2"].replace(",", "."))
        # En caso de que haya presentado un examen ordinario
        if usuario["Ordinario2"] != "":
            p2o = float(usuario["Ordinario2"].replace(",", "."))
            if p2o != "" and p2o > p2:
                p2 = p2o
    elif usuario["Ordinario2"] != "":
        p2 = float(usuario["Ordinario2"].replace(",", "."))
    else:
        p2 = 0

    if usuario["Practicas"] != "":  # Para los que hicieron la práctica
        pr = float(usuario["Practicas"].replace(",", "."))
        # Si volvieron hacer una práctica ordinaria:
        if usuario["OrdinarioPracticas"] != "":
            pro = float(usuario["OrdinarioPracticas"].replace(",", "."))
            if pro != "" and pro > pr:
                pr = pro
    elif usuario["OrdinarioPracticas"] != "":  # Para los que hiceron la ordinaria
        pr = float(usuario["OrdinarioPracticas"].replace(",", "."))
    else:  # Huevones no hicieron ni una práctica!
        pr = 0

    return p1, p2, pr


def nota_final(lista_dict):
    for x in lista_dict:
        p1, p2, pr = examenes(x)
        x["Final"] = str("{:.2f}".format((p1 * 0.3) + (p2 * 0.3)
                                         + (pr * 0.4))).replace(".", ",")
    return lista_dict


def evaluacion(lista_dict):
    A = []
    F = []
    for x in lista_dict:
        a = float(x["Asistencia"].replace("%", ""))
        b = float(x["Final"].replace(",", "."))
        if a >= 75:
            p1, p2, pr = examenes(x)
            if (p1 >= 4 and p2 >= 4 and pr >= 4):
                if (b >= 5):
                    A.append(x)
                else:
                    F.append(x)
            else:
                F.append(x)
        else:
            F.append(x)
    return A, F


dict_usuarios = nota_final(format_list("calificaciones.csv"))
aprobados, reprobados = evaluacion(dict_usuarios)
print("Alumnos aprobados, felicidades!: \n")
for x in aprobados:
    print(x)
print("\n\nAlumnos reprobados, sigan esforzandose!: \n")
for x in reprobados:
    print(x)
