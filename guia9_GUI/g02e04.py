#  Pedir el ingreso de 10 números y contar los mayores a 23.ç



import PySimpleGUI as sg
from fuimba import verificarInt
layout = [
            [sg.Text('      INGRESA 10 NUMEROS   ')],
            [sg.Text('Ingrese Numero'), sg.Input(key='numero')],
            [sg.Text(size=(40,1),key='cargar')],
            [sg.Text(size=(40,1),key='mayores')],
            [sg.Button('Cargar'), sg.Button('Exit'),sg.Button('Mostrar >23')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True
lisNum = []
c = 0
while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        verficar = verificarInt(values['numero'])
        if len(lisNum) < 10:
            if verficar[0]:
                lisNum.append(int(values['numero']))
                window['cargar'].update(f'Exito al cargar.')
                window['numero'].update('')
            else: 
                sg.popup('El numero ingresado no es valido')
        else:
            sg.popup('No puedes agregar mas numeros')
    elif event == 'Mostrar >23':
        for e in lisNum:
            if e > 23:
                c+=1
        sg.popup('Cantidad de numeros mayores a 23',c)

window.close()

