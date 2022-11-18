#Dada una lista cargada con 7 números enteros, obtener el promedio de ellos. 
#Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él.
#Dos funciones: promedio y mayorQue.

def promedio (num):
    prom = sum(num) / len(num)
    return prom 

def mayorQue (mayor, cantNumMayores):
    numMayor = [] 
    for x in range(len(cantNumMayores)):
        if mayor > cantNumMayores[x]:
            numMayor.append(cantNumMayores[x])  
    return numMayor
    
lista = []
for i in range(1,7):
    numero = int(input('Ingrese un numero entero: '))
    lista.append(numero)
print(lista)

print('El promedio de la lista es: ',promedio(lista))
print('Y el promedio es mayor a estos numeros de la lista')
print(mayorQue(promedio(lista),lista))