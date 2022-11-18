#Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto 
# que muestre el nombre del mayor y cuanto le lleva al menor.
#(Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

nombre1 = str(input('Ingrese un nombre: '))
edad1 = int(input('Ingrese la edad del primer nombre: '))
nombre2 = str(input('Ingrese otro nombre: '))
edad2 = int(input('Ingrese la edad del segundo nombre: '))
if edad1 > edad2:
    diferenciaEdades = edad1 - edad2
    cadena = str(nombre1) + ' le lleva una diferencia de ' + str(diferenciaEdades) + ' años a '+str(nombre2)
elif edad2 > edad1:
    diferenciaEdades = edad2 - edad1
    cadena = str(nombre2) + ' le lleva una diferencia de ' + str(diferenciaEdades) + ' años a '+str(nombre1)
else:
    cadena = str(nombre1)+' y '+ str(nombre2) +' tienen la misma edad.'

print(cadena) 