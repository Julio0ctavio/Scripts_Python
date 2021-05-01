'''El directorio de los clientes de una empresa está organizado en una
cadena de texto como la de más abajo, donde cada línea contiene la información
del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas
se separan con el carácter de cambio de línea \n y la primera línea contiene
los nombres de los campos con la información contenida en el directorio.'''

customers = {}
text = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
rows = text.split("\n")
titles = rows[0].split(";")
for x in range(1, len(rows)):
    user_data = rows[x].split(";")
    user = {}
    for y in range(1, len(user_data)):
        user[titles[y]] = user_data[y]
    customers[user_data[0]] = user

for x in customers.keys():
    print("{}: {}".format(titles[0], x))
    for y, z in customers[x].items():
        print("{}: {}".format(y, z))
    print("\n")
