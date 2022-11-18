#Definir una lista de 10 posiciones con letras. 
#Contar las vocales y mostrar el total.

def contarVocales (cadena):
    c = 0  
    for x in cadena:
        if x == 'a':
            c = c +1 
        elif x == 'e':
            c = c+1
        elif x == 'i':
            c = c+1
        elif x == 'o':
            c = c+1
        elif x == 'u':
            c = c+1        
    return c 
lista = []
for i in range(1,10):
    letra = input('Ingrese una letra: ')
    lista.append(letra)
print(lista)
print('La cantidad de vocales de la lista es ',contarVocales(lista)) 