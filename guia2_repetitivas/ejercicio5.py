#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.
#sueldos = int(input('Ingrese cuantos montos va a ingresar: '))

empleado = 'si'
total_sueldos = 0

while empleado == 'si':
    sueldo = int(input('Ingrese el sueldo correspondiente a ese empleado: '))
    total_sueldos = total_sueldos+sueldo
   
    empleado = input('Hay otro empleado para agregar? ')

print('_____________________________________________________________')
print('La suma de todos los sueldos ingresados es $',total_sueldos)
print('_____________________________________________________________')