#Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
# (Todos los días llovió distinta cantidad)


diasSemana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
lluvia = []
total = 0
mayor = 0
for x in range (7):
    mensaje = 'Cantidad de lluvia caida el dia '+str(x+1) + ': '
    ml_lluvia = float(input(mensaje))
    lluvia.append(ml_lluvia)

    total = total + ml_lluvia

    if ml_lluvia > mayor:
        mayor = ml_lluvia
for i in range (len(diasSemana)):
    if lluvia[i] == mayor:
        print('El total de lluvia de la semana es ', total,' milímetros y el día que mas llovió fue el ',diasSemana[i])











