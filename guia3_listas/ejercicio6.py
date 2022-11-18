#Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.

nombres = []
posicion = -1
datos = 'si'
while datos == 'si':
    nom = input('Ingrese un nombre: ')
    nombres.append(nom)
    datos = input('¿Desea seguir cargando personas? (si/no) ')

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

buscarNombre = str(input('Ingrese el nombre que quiere buscar en la lista: '))
print('En caso de no mostrar nada, es porque nombre no se encuentra en la lista')
print('_____________________________________________________________________')
for x in range (len(nombres)):
    if buscarNombre == nombres[x] :
        #resultadoBusqueda = len(nombres[x])
        print('Se ha buscado', buscarNombre, 'en la lista y se encuentra en la posicion', x )
    #else:
     #   print('El nombre que ha buscado no se encuentra en la lista')


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

for i in range(len(nombres)):
    if buscarNombre == nombres [i]:
        posicion = i

if posicion == -1:
    print('no ta')
else:
    print('Esta en la posicion',posicion)

