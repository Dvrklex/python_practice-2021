#Leer un número real y emitir una leyenda informando si es mayor o igual a cero 
# o bien es negativo (son dos opciones).

numero_real = input('Escribe un numero real: \r\n')
numero_real = int(numero_real)

if numero_real >= 0:
    print('El número que has ingresado es Positivo, es decir cero o mayor')
else:
    print('El número ingresado es negativo')

