'''Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones
múltiplos de 3, y muestre por pantalla la lista resultante.'''

import string

# El abecedario en español:
es_abc = list(string.ascii_lowercase + "ñ")
count = range(len(es_abc), 1, -1)
for x in count:
    if x % 3 == 0:
        es_abc.pop(x-1)
print(es_abc)
