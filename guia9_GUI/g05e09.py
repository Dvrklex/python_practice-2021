# Dada una lista cargada con números enteros, obtener el promedio de ellos.
#  Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él.


import PySimpleGUI as sg
from fuimba import verificarInt
layout = [
            [sg.Text('Ingrese Numero'), sg.Input(key='numero')],
            [sg.Text(size=(40,1),key='cargar')],
            [sg.Text(size=(60,1),key='promedio')],
            [sg.Button('Cargar'),sg.Button('Promedio'),sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True
lisNum = []
may = []
while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        valInt = verificarInt(values['numero'])
        if valInt[0]:
            lisNum.append(int(values['numero']))
            window['cargar'].update(f'Exito al cargar.')
            window['numero'].update('')
        else:
            sg.popup('El numero ingresado no es valido')
    elif event == 'Promedio':
        prom  = sum(lisNum) // len(lisNum)
        salida = ''
        for e in lisNum:
            if e > prom:
                may.append(e)
                salida +=  '- '+ str(e) + '\n'
        sg.popup(f'Los numeros mayores al promedio {prom} son:',salida)
        

window.close()