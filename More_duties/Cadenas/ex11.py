'''Escribir un programa que pregunte el nombre de un producto, su precio y un
número de unidades y muestre por pantalla una cadena con el nombre del producto
seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
import argparse


def operation():
    precio_unitario = "{:9.2f}".format(args.precio)
    unidades = args.unidades
    print("Producto -> {}".format(args.nombre))
    print('Unidades -> {uni:3d} \n Precio Unitario $ {pre} \n Total $ {t:11.2f}'.format(
        uni=unidades, pre=precio_unitario, t=float(precio_unitario) * unidades))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nombre", type=str, required=True,
                        help="Nombre del producto", default=None)
    parser.add_argument("-p", "--precio", type=float, required=True,
                        help="Precio del producto", default=None)
    parser.add_argument("-u", "--unidades", type=int, required=True,
                        help="Catidad de prodcutos", default=None)
    args = parser.parse_args()
    operation()
