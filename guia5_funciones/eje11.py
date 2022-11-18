#Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
def lluvia():
    dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    myc = 0
    suma = 0
    for i in range(7):
        llovido = input('Ingrese los milimetros llovidos: ')
        llovido = int(llovido)
        suma += llovido
        if llovido > myc:
            myc = llovido
            dml = dias[i]
    return suma,dml
final = lluvia()
print('El total de lluvia caido en la semana y el dia que mas llovio son:')
print(final)