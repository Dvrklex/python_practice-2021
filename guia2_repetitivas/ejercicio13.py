#Ingresar la lluvia caída en milímetros para cada día de la semana.
#  Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.
print('Te pedire que ingreses la cantidad de milimetros llovidos en cada dia de la semana')
print('Si en un dia no llovio coloque 0')
diasSinLluvia = 0
lluviaTotal = 0
for i in range (1,8):
    diaSemana = input('Ingrese el dia de la semana: ')
    ml_lluvia = float(input('Ingrese la cantidad de milimetros: '))
    if ml_lluvia > 0:
        lluviaTotal = lluviaTotal + ml_lluvia
    else:
        diasSinLluvia = diasSinLluvia+1

print('Los milimetros total de lluvia son:', lluviaTotal,'milimetros')

print('Estos son la cantidad de dias que no han llovido:', diasSinLluvia)


#mensaje = 'Cantidad de lluvia caida el dia ' + str(x+1) + ': '















