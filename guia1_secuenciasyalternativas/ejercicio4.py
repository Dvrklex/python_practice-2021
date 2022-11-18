#Leer dos números y decir cuál es el mayor.
primer_numero = input('Ingrese un número entero: \r\n')
primer_numero = int(primer_numero)
segundo_numero = input('Ingrese otro número entero:\r\n')
segundo_numero = int(segundo_numero)

if primer_numero > segundo_numero:
    print('El número', primer_numero,'es mayor a', segundo_numero)
elif primer_numero == segundo_numero:
     print('Ambos numeros son iguales')
else:
    print('El número', segundo_numero,'es mayor a', primer_numero)