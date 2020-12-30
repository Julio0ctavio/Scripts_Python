##############
## PROBLEMA DE LA MOCHILA
####################
import random

class Mochila:
    def __init__(self, peso, capacidad):
        self.peso = peso
        self.capacidad = capacidad


    def meterObjeto(self, objeto):
        self.peso += objeto.peso



class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valorporunidad = self.valor/self.peso


#algoritmo de ordenación por selección
def selectionsort(lista,tam):
        for i in range(0,tam-1):
            min=i
            for j in range(i+1,tam):
                if lista[min].valorporunidad > lista[j].valorporunidad:
                    min=j
            aux=lista[min]
            lista[min]=lista[i]
            lista[i]=aux

mochila = Mochila(0, 100)
objetos = []
num_obj = int(input("Ingrese el numero de elementos al análisis:"))
x = 0

while x < num_obj:
    objetos.append(Objeto(random.randint(1,40),random.randint(1,8)))
    x = x + 1;

selectionsort(objetos, len(objetos))
resultado = []
interes = []
precio = []
peso = []

for i in range(len(objetos)):
    resultado.append(0)
    interes.append(0)
    precio.append(0)
    peso.append(0)

i = len(objetos) - 1

#empezamos desde el final porque están ordenados de menor a mayor
while(mochila.peso < mochila.capacidad):
    objeto = objetos[i]
    if ((mochila.peso + objeto.peso) <= mochila.capacidad):
        resultado[i] = 1
        peso[i] = objeto.peso
        precio[i] = objeto.valor
        interes[i] = objeto.valorporunidad
        mochila.meterObjeto(objeto)
    else:
        resultado[i] = (mochila.capacidad - mochila.peso) / objeto.peso
        mochila.peso = mochila.capacidad
    i-=1

print ("Resultado: Selección de los objetos según su Interés")
y = 1
for i in range(len(resultado)-1, -1, -1):
    if(resultado[i] == 1):
        print ("Articulo ",y, "Peso: ", peso[i], "Precio: ", precio[i]," -> Interés: ", interes[i])
        y = y + 1
    else:
        break;
