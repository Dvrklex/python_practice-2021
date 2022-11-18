#  Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una
# pregunta = input('Desea comenzar una lista de personas? (si/no)')


import PySimpleGUI as sg

layout = [
            [sg.Text('Nombre:'), sg.Input(key='nombre')],
            [sg.Radio('Masculino','SEXO1',key='mas'),sg.Radio('Femenino','SEXO1',key='fem')],
            [sg.Text(size=(70,1),key='total')],
            [sg.Text(size=(40,1),key='ver')],
            [sg.Button('Cargar'),sg.Button('Mostrar'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True
lMujeres = []


while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':      
        if values['fem']:
            lMujeres.append(values['nombre'])
            window['ver'].update('Nombre cargado')
            window['nombre'].update('')
        else:
            window['ver'].update('Nombre cargado')
            window['nombre'].update('')
    elif event =='Mostrar':
        salida = ''
        for e in lMujeres:
            salida += '- '+ e.capitalize() + '\n' 
        sg.popup(f'La cantidad de mujeres de la lista es {len(lMujeres)}',salida)
window.close()




