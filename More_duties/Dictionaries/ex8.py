'''Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos
puntos, y cada par <palabra>:<traducción> separados por comas.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla
palabra a palabra. Si una palabra no está en el diccionario debe dejarla
sin traducir.'''

esp_eng = {}
sentence_translated = ""
cierre = True
while cierre:
    key = input("Introduzca su palabra con su par en inglés <esp>:<eng> \n")
    words = key.split(":")
    esp_eng[words[0]] = words[1]
    cierre = input("¿Desea continuar agregando pares? y/n: ") == "y"
sentence = input("Ingrese su oración: \n")
words = sentence.split()
for x in words:
    if x in esp_eng.keys():
        sentence_translated += esp_eng[x] + " "
    else:
        sentence_translated += x + " "
print("Traducción al inglés: {}".format(sentence_translated))
