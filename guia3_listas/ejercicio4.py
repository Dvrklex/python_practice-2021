#Dada una lista con números, crear otra con los cuadrados de esos valores. 

listaNumeros = []

num_al_cuadrado = []
for i in range(5):
    numero = int(input('Ingrese un numero: '))
    num_al_cuadrado.append(pow(numero,2))
print(num_al_cuadrado)

#recorrido por indicacion
#solucion  2 
#cuadrados = []
#for i range (len(n)):
    #cuadrado = n[i] * n[z]
    #cuadrados.append(print('------------------------------------------------------------------------------------------')cuadrado)
#print(cuadrado)


#recorrido por elemento
#for e in n:
#    cuadrados.append(e*e)
#print(cuadrado)





