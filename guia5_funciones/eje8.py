#Ingresar nombres , 
#luego buscar un nombre y de encontrarlo decir en qué posición está.
def nameSearch (): 
    nombresLista = []
    posName = 0 
    for i in range(0,4):
            name = input('Ingrese un nombre: ')
            nombresLista.append(name)
    buscar = input('Ingrese el nombre que quiere buscar en la lista: ')
    for b in range (len(nombresLista)):
        if buscar == nombresLista[b] :
            posName = b
    return posName
print(nameSearch())


