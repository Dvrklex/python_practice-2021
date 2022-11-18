#  Preguntar cuántas personas se van a cargar y luego solicitar sus edades, 
# mostrando al final la edad promedio.


import PySimpleGUI as sg
from fuimba import verificarInt
layout = [
            [sg.Text('Nombre'), sg.Input(key='nombre')],
            [sg.Text('Edad'), sg.Input(key='edad')],
            [sg.Text(size=(40,1),key='cargar')],
            [sg.Text(size=(40,1),key='promedio')],
            [sg.Button('Cargar'), sg.Button('Exit'),sg.Button('Calcular Promedio')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True
lisEdad = []
while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        valEdad = verificarInt(values['edad'])
        if valEdad[0]:
            lisEdad.append(int(values['edad']))
            window['edad'].update('')
            window['nombre'].update('')
        else:
            sg.popup('La edad ingresada no es valida')
    elif event == 'Calcular Promedio':       
        prom = sum(lisEdad) // len(lisEdad)
        sg.popup('Promedio de edades',prom)

window.close()