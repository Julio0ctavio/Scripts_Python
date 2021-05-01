'''Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura,
pagar una existente o terminar. Si desea añadir una nueva factura se preguntará
por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se
eliminará del diccionario. Después de cada operación el programa debe mostrar
por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente
de cobro.'''

facturas = {}
cierre = True
cobro = 0
pendiente = 0
print("Ingrese la opción deseada: \n a) Añadir factura\n b) Pagar factura\n c) Terminar\n")
while cierre:
    x = input()
    if x == "a":
        key = input("Ingrese el N° de Factura: ")
        value = float(input("Factura N°{} con un importe de: $ ".format(key)))
        facturas[key] = value
        pendiente += value
    if x == "b":
        key = input("Ingrese el N° de Factura: ")
        if key in facturas.keys():
            print("Factura N°{} ha sido pagada con un total de $ {:,}"
                  .format(key, facturas[key]))
            cobro += facturas[key]
            pendiente -= cobro
            del(facturas[key])
        else:
            print("La factura N° {} no existe...")
    if x == "c":
        cierre = False
    print("Monto cobrado: $ {:,} \nMonto pendiente por cobrar: $ {:,}"
          .format(cobro, pendiente))
