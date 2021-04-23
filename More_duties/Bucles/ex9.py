'''Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que
introduzca la contraseña correcta.'''

from werkzeug.security import check_password_hash, generate_password_hash


def verify_password(password_h, password):
    return check_password_hash(password_h, password)


def create_password_hash(password):
    return generate_password_hash(password)


password = input("Ingrese su password: \n")
password_h = create_password_hash(password)
verify = False

while verify is False:
    pass_confirm = input("Confirme su password: ")
    verify = verify_password(password_h, pass_confirm)

print("Se ha verificado correctamente su password! :)")
