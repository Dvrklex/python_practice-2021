#Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

personas = int(input('cuantas personas de van a cargar? \r\n'))
listaEdades = []
for i in range(personas):
    edades = int(input('Ingrese la edad: \r\n'))
    listaEdades.append(edades)

print(listaEdades)
for r in (listaEdades, 0):
    print(sum(listaEdades)//personas) 



