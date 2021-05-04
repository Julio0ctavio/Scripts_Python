'''Escribir una función que pida un número entero entre 1 y 10 y guarde en
un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
done n es el número introducido.'''


def request():
    n = int(input("Ingrese un número entero (1-10): "))
    with open("tabla-{}.txt".format(n), "w") as file:
        for i in range(1, n+1):
            file.write("{} * {} = {} \n".format(n, i, n*i))
            print("{} * {} = {}".format(n, i, n*i))


request()
