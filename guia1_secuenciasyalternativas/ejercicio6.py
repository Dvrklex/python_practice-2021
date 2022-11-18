#Leer dos números y luego una opción (puede ser '+' o '-'),
#  y según la opción elegida realizar el cálculo.


numero1 = input('Ingrese un número: \r\n')
numero1 = int(numero1)
numero2 = input('Ingrese otro número: \r\n')
numero2 = int(numero2)
operacion = input('Introduzca + para sumar o - para restar \r\n')
    
if (operacion == '+'):
        print('La suma entre ambos numeros es igual a',numero1 + numero2)
elif (operacion == '-'):
    print( 'La resta entre ambos numeros es igual a', numero2 - numero1)
else: 
    print('Has ingresado datos invalidos, intenta denuevo, manco')



