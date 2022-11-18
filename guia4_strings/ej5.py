#Recibir por teclado una cadena de números e insertar  un punto cada 3 dígitos como divisorio de miles.
#  Ej.  1234567890 debería devolver 1.234.567.890


num = input ('Ingrese el numero: ')
num1 = list(num)


for i in range(len(num1),0,-3):
    num1.insert(i,'.')
punto=''.join(num1)
print(punto[:-1])







