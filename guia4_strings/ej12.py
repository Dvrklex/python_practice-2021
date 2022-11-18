#Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. 
# Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 57 pesos casi seguro’,
#   mostraría 114.


# cadena = input('Ingrese un texto que contenga almenos un numero: ')
# #print(cadena)
# #lis= []
# lis = ''
# numbers = [int(cadena)for cadena in cadena.split() if cadena.isdigit()]
# for x in numbers:
#     # num = x*2
#     lis = x
#     #lis.append(num) #esto es si fuera para agregarlo a otra lista 

# print(lis)




#POSIBLE SOLUCION 2 
frase = input ('Ingrese una frase con almenos un digito: ')
num1 = ''
for numero in frase:
    if numero in '0123456789':
       num1 = num1+numero

print(int(num1)*2)
