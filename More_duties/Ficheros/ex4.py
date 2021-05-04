'''Escribir un programa que acceda a un fichero de internet mediante su url
y muestre por pantalla el número de palabras que contiene.'''


def words_file(url):

    from urllib import request
    from urllib.error import URLError
    try:
        file = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = file.read()
        print("Conteo de Palabras del sitio '{}':".format(url))
        return len(content.split())


print(words_file('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(words_file('https://no-existe.txt'))
