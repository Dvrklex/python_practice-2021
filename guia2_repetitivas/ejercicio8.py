#Ingresar autos y sus precios y contar cuantos valen entre $1.460.000 y $2.850.000.
#  Terminar la carga cuando el valor ingresado sea $0.

precio_coches = int(input('Ingrese el precio del coche: '))

c = 0
while precio_coches > 0:
    precio_coches = int(input('Ingrese el precio otro coche: '))
    print('Para dejar de agregar precios, coloce 0')
    if  precio_coches > 1400000 and precio_coches < 2850000:
        c = c + 1
print('La cantidad de coches con precio entre $1.450.000 y $2.850.800 es $',c)



     






















