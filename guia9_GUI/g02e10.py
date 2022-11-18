# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo 
#  y mostrar el nombre de la persona que menos gana.
import PySimpleGUI as sg
from fuimba import verificarInt
layout = [
            [sg.Text('Nombre'), sg.Input(key='nombre')],
            [sg.Text('Sueldo'), sg.Input(key='sueldo')],
            [sg.Text(size=(40,1),key='minimo')],
            [sg.Button('Cargar'),sg.Button('Sueldo Minimo'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True
infinite = 1e309
lPersonas = []
lSalarios = []
while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        val = verificarInt(values['sueldo'])
        if val[0]:
            lPersonas.append(values['nombre'])
            lSalarios.append(int(values['sueldo']))
            window['nombre'].update('')
            window['sueldo'].update('')
        else:
            sg.popup('El sueldo ingresado no es valido')
    if event == 'Sueldo Minimo':
        minimo = min(lSalarios)
        elMasPobreton =''
        for x in range (len(lPersonas)):
            if lSalarios[x] == minimo:
                elMasPobreton +='> ' +lPersonas[x] + ' - $' + str(minimo) + '\n'
        sg.popup('La/s peroas que menos gana/n es/son',elMasPobreton)
        




window.close()