#Cargar en dos listas paralelas nombres y sueldos.
#  Luego mostrar los nombres de las personas que ganan más de $85000.


cant_sueldos = []
nombresQueMasGanan = []
datos = 'si'

while datos == 'si':
    nombres = input('Ingrese un nombre: ')
    sueldo = int(input('Ingrese el monto del sueldo: '))
    cant_sueldos.append(sueldo)
    if sueldo > 85000:
        nombresQueMasGanan.append(nombres)
        
    datos = input('Desea cargar mas sueldos? (si/no) \r\n')

print('Estas son las personas con un salario mayor a $85.000')
print(nombresQueMasGanan)      

