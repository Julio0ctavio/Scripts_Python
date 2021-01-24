# How to find the first non repeated character of a given String?
string = "Hola hamigos"
string = string.lower()

afir = string[0]
found = 0

for i in string[1:]:
    if i == afir:
        found = found + 1
        afir = string[found]

print(afir)

# Given a set of strings, find the longest common prefix.
# "aaa","aab","aac", "aaaaad"  ⇒ "aa"

aux = 0
string = []
string = "aaa", "aab", "aac", "aaaaad"
prefixes = []
prefix = ""

# Iniciamos el primer ciclo para verificar los strings:
for element in string:
    # En el segundo ciclo analizaremos la posición inicial con una posición después:
    for i in element[1:]:
        # Si ambas posiiones coinciden, las concatenamos en un prefix:
        if (i == element[aux]) and aux == 0:
            prefix = prefix + i + element[aux]
        # Si no, se vuelve a validar la posición siguiente, después de la inicial:
        elif(i == element[aux]):
            prefix = prefix + i
        # Actualizamos el auxiliar:
        aux += 1
        # En caso de que aux tenga el valor de la longitud del string:
        if aux == len(element)-1:
            break
    prefixes.append(prefix)
    prefix = ""
    aux = 0

# Ahora comparamos el conteo del prefix de cada string:
print(prefixes)
aux_prefix = 0
longest = ""
# En el ciclo anterior se considera el prefix que más veces se presenta en la lista:
for i in prefixes[1:]:
    if prefixes.count(i) >= prefixes.count(prefixes[aux_prefix]):
        longest = i
    aux_prefix = aux_prefix + 1
print("Longest -> {}".format(longest))
