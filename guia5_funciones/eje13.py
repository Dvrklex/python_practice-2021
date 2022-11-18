#Pedir el ingreso de un nombre completo (Juan Pérez)
#  y mostrarlo invertido y con coma (Pérez, Juan).

def invertirNombre (invertir):
    vuelta = invertir.split()
    name = vuelta[1] + ', ' + vuelta[0]
    return name
a = str(input('Ingrese el nombre y apellido, en el orden mencioando: '))

print(invertirNombre(a))
