def dividir(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("¡división por cero!")
    finally:
        print("el resultado es " + str(result))


def other():
    try:
        x = int(input("Ingrese un número: "))
        num = 4/0
        a + 45
        'julio' + 99
    except ZeroDivisionError:
        print("División entre cero")

    except SyntaxError:
        print("Escribe bn el código animal... das lástima")

    except NameError:
        print("No se ha definido la variable 'a'")

    except TypeError:
        print("No puedes sumar el string 'julio' con un valor numérico")

    except ValueError:
        print("¿Está pendejo emi? eso no es un número...")


'''Podemos utilizar una excepción en la función y a su vez que me
indique un resultado en la clausula finally'''


dividir(2, 1)
other()
