#El costo del pasaje a Córdoba es de $1700. La empresa realiza un descuento de un 40 % sobre el costo 
# del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65).
#  Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
nombre = input('Ingrese su nombre y apellido: \r\n')
edad = int(input('Por favor ingrese su edad: \r\n'))
descuento_pasaje = 1700 * 0.40
costo_final = int(descuento_pasaje)

if edad <= 10 and edad >= 5 or edad >= 65:
    print(nombre, 'el costo final de su pasaje es $', costo_final)
else:
    print(nombre, 'el costo de su pasaje es $1700')
