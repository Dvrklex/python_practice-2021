#Realizar un algoritmo que permita ingresar un dato numérico
#  y determinar si es un número positivo de dos dígitos.

numero = input('Ingrese un número: \r\n')
numero = int(numero) 

if numero >= 10:
    print('Este es un número positivo compuesto por 2 o mas dígitos.')

else: 
    print('ERROR, ingresa un número mayor a 10.')


