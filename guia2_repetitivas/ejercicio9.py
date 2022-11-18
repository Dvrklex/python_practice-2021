#Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. 
# Se deberá ir preguntando si hay más números para ingresar.


numeros = (5,4,3,54,36,44,12,32,477,8,98)
maximo = numeros[0]
for i in numeros:
    if i > maximo:
        maximo = i

print('El numero maximo es', maximo)






