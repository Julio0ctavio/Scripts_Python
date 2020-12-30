print("Serie Fibonacci")


def fib(n):

    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        # Imprimir los datos de manera horizontal
        print(str(b), end=' ')


print("n = 50")
fib(50)
print("\n")


def fib2(n):
    # escribe la serie de Fibonacci hasta n
    resultado = []
    a, b = 0, 1

    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

# Ahora llamamos a la funcion que acabamos de definir:


fibo = fib2(2000)

# Imprime la lista "resultado" que está incluida en el método fib2
print("Dado que n sea igual a: " + "\n" + str(fibo))
