#Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y decir si es negativo o no.
#  Preguntar si repite.

datos = input('Tienes datos para ingresar? (si/no) \r\n')

while datos == 'si':
    numero_entero = int(input('Ingresa un numero entero: \r\n'))
    if numero_entero > 0:
        print('Has ingresado un numero positivo')
    else:
        print('Has ingresado un numero negativo')
    
    datos = input('repite? (si/no) \r\n')

print('Hasta Luego')
    
    
    
    