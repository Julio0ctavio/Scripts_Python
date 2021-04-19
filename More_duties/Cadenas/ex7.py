'''Escribir un programa que pregunte el correo electrónico del usuario en la
consola y muestre por pantalla otro correo electrónico con el mismo nombre
(la parte delante de la arroba @) pero con dominio ceu.es.'''

import re


mail = input("Introduce el correo: \n")
new_mail = re.sub(r"@(.+)", "@ceu.es", mail)
print("Nuevo correo -> {}".format(new_mail))
