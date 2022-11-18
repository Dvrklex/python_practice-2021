#Leer dos números reales y mostrarlos en orden creciente.
primer_numero = input('Ingrese un número entero: \r\n')
primer_numero = int(primer_numero)
segundo_numero = input('Ingrese otro número entero:\r\n')
segundo_numero = int(segundo_numero)

if primer_numero > segundo_numero:
    print(segundo_numero,',', primer_numero)
else:
    print(primer_numero,',', segundo_numero)