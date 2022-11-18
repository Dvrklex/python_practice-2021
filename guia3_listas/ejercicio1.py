#(4 de la guía 2) Pedir el ingreso de 10 números. Contar los mayores de 23.
#Almacenar los que cumplen la condición.  Mostrar los resultados.

listaNumeros = []

c = 0
for i in range(10):
    numero = int(input('Ingrese un numero: '))
    
    if  numero > 23:
        c = c + 1
        listaNumeros.append(numero)
print('La cantidad de numeros mayores a 23 es', c)
print(listaNumeros)










