def pares(limite):

    num = 1

    while num < limite:

        # La diferencia entre una función y un generador, es el campo yield...

        yield num*2

        num = num + 1


generador = pares(10)

for x in generador:

    print(x)


def familia(*miembro):
    for x in miembro:

        # En caso de que yo necesite la letra de un registro especifico el yield con 'from'

        yield from x


fam = familia('Julio', 'Moy', 'Miriam', 'Octavio')

print(next(fam) + next(fam) + next(fam) + next(fam) + next(fam), end=' ')
