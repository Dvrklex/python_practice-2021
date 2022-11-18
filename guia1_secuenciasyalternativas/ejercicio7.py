#Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
nombre = input('Ingrese su nombre: \r\n')
edad = input('Ingrese su edad: \r\n')
edad = int(edad)

if edad >= 18:
    print('Usted puede votar.')
else:
    print('Aun no puedes votar, vuelve cuando tengas 18 años.')