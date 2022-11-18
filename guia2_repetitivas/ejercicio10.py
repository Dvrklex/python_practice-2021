#Dada una lista de nombres y de salarios respectivos, 
#determinar el salario mínimo y mostrar el nombre de la persona que menos gana.

sueldoMasBajo = 10000000000

for i in range (3):
    nombre = input('Ingrese el nombre del empleado: ')
    sueldo = int(input('Ingrese el monto del salario: '))
    if sueldo < sueldoMasBajo:
        sueldoMasBajo = sueldo
        elMasPobreton = nombre
print('La persona que menos gana es', elMasPobreton, 'y gana $',sueldoMasBajo)





















