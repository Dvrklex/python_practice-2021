#Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.
pregunta = input('Desea elegir metodo de pago (si/no): ')
listaPersonas = []
listaMujeres = []
mujeres = 0
pregunta = 'si'
while pregunta == 'si':
    print('Metodos de pago')
    print('1 = efectivo')
    print('2 = online')
    sexo = int(input('Ingrese un metodo de pago: '))
    if sexo == 2:
        nombre = input('Ingrese un nombre: ')
        listaMujeres.append(nombre)
        listaPersonas.append(nombre)
        mujeres = mujeres+1
    else:
        nombre = input('Ingrese un nombre: ')   
        listaPersonas.append(nombre)     
    pregunta = input('Desea seguir agregando personas a la lista? (si/no) \r\n')

print('_____________________________________________________________________')     
print('-----> LA CANTIDAD DE MUJERES DE LA LISTA ES' ,mujeres, '<-----')
print(listaMujeres)
print('_____________________________________________________________________')
print('_____________________________________________________________________')
print('Esta es la lista de todos las personas que has agregado a la lista:')
print(listaPersonas)
print('_____________________________________________________________________')
