#Pasar un período expresado en segundos a un período
#  expresado en días, horas, minutos y segundos.

segundos = int(input('Escriba la cantidad de segundos: \r\n'))

dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60

print('Dias: {} - Horas: {} - Minutos: {} - Segundos: {}'. format(dias,horas,minutos,segundos))


