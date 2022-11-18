#Cargar una lista con números. 
#Invertir los elementos (sin usar reverse). 
#Mostrar.
def invertirLista (darVuelta):
    numLista = darVuelta[::-1]
    return numLista

lista = []
for i in range(0,7):
    numero = int(input('Ingrese un numero entero: '))
    lista.append(numero)
print(lista)

print('La lista invertida es: ', invertirLista(lista))