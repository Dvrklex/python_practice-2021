#  Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

import PySimpleGUI as sg

layout = [
            [sg.Text('Nombre'),sg.Input(key='nombre')],
            [sg.Text('Apellido'), sg.Input(key='apellido')],
            [sg.Text(size=(40,1),key='invertir')],
            [sg.Button('Invertir'), sg.Button('Salir')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Salir']:
        break
    if event == 'Invertir':
        window['invertir'].update(f'Hola {values["apellido"]} {values["nombre"]}.')
        window['nombre'].update('')
        window['apellido'].update('')
    

window.close()