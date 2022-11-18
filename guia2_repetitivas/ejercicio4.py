#Pedir el ingreso de 10 números. Contar los mayores de 23. Mostrar el resultado.
print ('Te pedire que ingreses 10 numeros enteros')
print('____________________________________')
c = 0
for i in range(10):
    numero = int(input('Ingrese un numero: '))
    if  numero > 23:
        c = c + 1
print('La cantidad de numeros mayores a 23 es', c)
















