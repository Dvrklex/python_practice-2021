#Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez)
#  y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).


a = str(input('Ingrese el nombre y apellido, en el orden mencioando: '))
b = a.split()           #Convertir a en una lista.

print(b[1],b[0])    #Imprime primero el valor 1 de la lista, y luego el valor 0.


