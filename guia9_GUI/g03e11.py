# Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad.
from datetime import datetime,date

def fecVal(fec):
    validado = False 
    while not validado:
        fecha= fec
        try:
            fech = datetime.strptime(fecha, '%d-%m-%Y') #pasar a formato dia mes año
            validado = True
            return True,fecha
        except :
            validado = True
            return False,''

def edad(anios): #Calcular edad con el import date (datetime)
    validado = False
    fn = anios
    try:
        hoy = date.today()
        dn, mn, an = fn.split('-')
        dn = int(dn)
        mn = int(mn)
        an = int(an)
        dh = int(hoy.day)
        mh = int(hoy.month)
        ah = int(hoy.year)
        e = ah - an
        
        if (mn > mh) or (mn == mh and dn > dh):
            e -= 1
            validado = True
            return e
        else:
            return e 
    except:
        pass
    
    

import PySimpleGUI as sg

layout = [
            [sg.Text('Nombre'),sg.Input(key='name')],
            [sg.Text('Fecha de nacimiento'), sg.Input(key='fecnac')],
            [sg.Text(size=(40,1),key='mayores')],
            [sg.Button('Cargar'),sg.Button('Mayores Edad'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

lNames= []
lFechas  = []


while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        validar = fecVal(values['fecnac'])
        if validar[0]:
            lNames.append(values['name'])
            lFechas.append(values['fecnac'])
            
        else:
            sg.popup('La fecha ingresada no es valida')
    if event == 'Mayores Edad':
        salida = ''
        for fechas in range(len(lFechas)):
            años = edad(lFechas[fechas])
            if int(años) >= 18: 
                salida += '> ' + lNames[fechas] + '\n'
        sg.popup('Los mayores de edad son',salida)
window.close()

