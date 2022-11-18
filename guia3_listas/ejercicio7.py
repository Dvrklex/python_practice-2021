#Dada una lista cargada con 7 números enteros, obtener el promedio. 
#Mostrar por pantalla dicho promedio y los números de la lista que sean mayores que él.
print('Te pedire que ingreses 7 numeros para agregarlos a una lista')
listaNumeros = []
numeros_mayorDeLa_lista_mayor_al_promedio = []

for i in range (7):
    num = int(input('Ingrese un numero: '))
    listaNumeros.append(num)

#listaNumeros = sum(listaNumeros)
promedio = (sum(listaNumeros)) // 7
resultadoPromedio = promedio
for i in range (7):
    if listaNumeros[i] > resultadoPromedio:
        numeros_mayorDeLa_lista_mayor_al_promedio.append(listaNumeros[i])

print('Este es el promedio de todos los numeros ingresados:', resultadoPromedio)
print('________________________________________________________________________')
print('He colocado los numeros ingresados que sean mayores al promedio de la lista: ')
print(numeros_mayorDeLa_lista_mayor_al_promedio)