# input de fechas (validar formato y devolver año, mes y día como enteros),
#  debe forzar un formato estricto, por ejemplo dd/mm/aaaa.
from datetime import datetime
def fecVal(mensaje):
    error = '*Sonido de error* La fecha ingresada no es valida.'
    validado = False 
    while not validado:
        fecha= input(mensaje)
        try:
            fec = datetime.strptime(fecha, '%d/%m/%Y') #pasar a formato dia mes año
            print('Fecha valida.')
            validado = True
        except :
            print(f'{error}')
    return fecha
fec = fecVal('Ingrese fecha (dd/mm/aaaa): ')

dma = ['Dia','Mes','Año']
formato = fec.split('/')
for e in range (len(formato)):
    print(dma[e],'-->',formato[e])