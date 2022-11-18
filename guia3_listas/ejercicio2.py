#Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

print('Vamos a crear una lista de letras')
datos = input('Desea comenzar la lista? (si/no) ')
listaLetras = []
c = 0
while datos == 'si':
    letras = str(input('Ingrese aqui una letra: '))
    listaLetras.append(letras)
    datos = input('Desea seguir agregando letras a la lista? (si/no) \r\n')
#para recorrer la lista listraLetras tengo que poner el x que va indentando por cada elemento de la lista
for x in listaLetras:      
    if  x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            c = c+1
        
print('La cantidad de vocales de la lista es', c)
print(listaLetras)



    
    
    














