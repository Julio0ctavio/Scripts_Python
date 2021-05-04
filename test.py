# How to find the first non repeated character of a given String?
string = "Hola amigos".replace(" ", "").lower()
letter = ""
for x in string:
    if string.count(x) == 1:
        letter = x
        break
print(letter)

# Given a set of strings, find the longest common prefix.
# "aaa","aab","aac", "aaaaad"  ⇒ "aa"
'''
input->   "aaa", "aab", "aac", "aaaaad"
output <- aa
input->   "aaca", "aacb", "aacb", "aacaaad"
output <- aac
input->   "a1a", "a1ab", "a3ac", "a1"
output <- a
input->   "a1a", "a1ab", "a13ac", "a1"
output <- a1
'''
strings = []
strings = "a1a", "a1ab", "a13ac", "a1"
count = 0
prefix = ""

# Se recorrerá el vector strings:
for word in strings:
    # Se analizará cada elemento de la palabra:
    for i in word:
        prefix = prefix + i
        # En este caso se propone leer el primer string:
        for j in range((len(strings) - 1), 0, -1):
            # Si el prefix se encuentra en la palabra [j] del vector strings:
            if prefix in strings[j]:
                # Contará el numero de veces que se presente en las palabras del
                # vector strings
                count += 1
            else:
                # Si no coincide, se indica el elemento encontrado:
                prefix = prefix[0:len(prefix)-1]
                count = 0
                break
        if count == 0:
            break
    if count == 0:
        break

print("Longest -> {}".format(prefix))
