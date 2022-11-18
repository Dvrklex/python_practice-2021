# Pedir dos números enteros, sumarlos y mostrar el resultado.
import PySimpleGUI as sg
from fuimba import verificarInt

layout = [
        
        [sg.Text('Primer numero'),sg.Input(key='num1')],
        [sg.Text('Segundo numero'), sg.Input(key='num2')],
        [sg.Text(size=(40,1),key='resultado')],
        [sg.Button('Sumar'), sg.Button('Restar'),sg.Button('Multiplicar'),sg.Button('Dividir'),sg.Button('Exit')]
        ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    
    if event == 'Sumar':
        verificar1 = verificarInt(values['num1'])
        verificar2 = verificarInt(values['num1'])
        if verificar1[0] == True and verificar2[0] == True:            
            sg.popup('Resultado',f'{values["num1"]} + {values["num2"]}  = {int(values["num1"])+int(values["num2"])}')
            window['num1'].update('')
            window['num2'].update('')
        else:
            sg.popup('Has ingresado numeros incorrectos')
    elif event == 'Restar':
        verificar1 = verificarInt(values['num1'])
        verificar2 = verificarInt(values['num1'])
        if verificar1[0] == True and verificar2[0] == True:
            sg.popup('Resultado',f'{values["num1"]} - {values["num2"]}  = {int(values["num1"])-int(values["num2"])}')
            window['num1'].update('')
            window['num2'].update('')
        else:
            sg.popup('Has ingresado numeros incorrectos')
    elif event == 'Multiplicar':
        verificar1 = verificarInt(values['num1'])
        verificar2 = verificarInt(values['num1'])
        if verificar1[0] == True and verificar2[0] == True:
            sg.popup('Resultado',f'{values["num1"]} * {values["num2"]}  = {int(values["num1"])*int(values["num2"])}')
            window['num1'].update('')
            window['num2'].update('')
        else:
            sg.popup('Has ingresado numeros incorrectos')
    elif event == 'Dividir':
        verificar1 = verificarInt(values['num1'])
        verificar2 = verificarInt(values['num1'])
        if verificar1[0] == True and verificar2[0] == True:
            sg.popup('Resultado',f'{values["num1"]} / {values["num2"]}  = {int(values["num1"])//int(values["num2"])}')
            window['num1'].update('')
            window['num2'].update('')
        else:
            sg.popup('Has ingresado numeros incorrectos')
window.close()