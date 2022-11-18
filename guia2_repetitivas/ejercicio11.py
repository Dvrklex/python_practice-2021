#Ingresar 7 números enteros y en el caso de que sean naturales
#  de una sola cifra mostrar un cartel en cada uno.

print ('Te pedire que ingreses 7 numeros enteros')
print('____________________________________')
n_unacifra = []
c = 0
for i in range(7):
    numero = int(input('Ingrese un numero: '))
    if  numero < 10 and numero >= 1:
        c = c + 1
        n_unacifra.append(numero)
print('Estos son los numeros ingresados que son naturales de una sola cifra son', c)
print(n_unacifra)






