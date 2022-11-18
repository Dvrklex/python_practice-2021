#Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad.
personas = []
edades = []
mayoresDeEdad= []
datos = 'si'

while datos == 'si':
    nombres = input('Ingrese un nombre: ')
    edad = int(input('Ingrese la edad: '))
    edades.append(edad)
    if edad >= 18:
        mayoresDeEdad.append(nombres)
        personas.append(nombres)
    else:
        personas.append(nombres)
        
    datos = input('¿Desea cargar mas datos? (si/no) \r\n')

print('Estas son las personas mayores de edad')
print(mayoresDeEdad)      














