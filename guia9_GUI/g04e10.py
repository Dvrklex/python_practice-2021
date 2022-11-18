# Determinar cuál es la vocal que aparece con mayor frecuencia en una frase.
             
import PySimpleGUI as sg

layout = [
            [sg.Text('Ingrese una frase'), sg.Input(key='frase')],
            [sg.Text(size=(40,1),key='salida')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'OK':
        vocales = {}
        lVocales = ['a','e','i','o','u']      
        for t in values['frase'].lower(): 
            if t in lVocales:           
                if t not in vocales.keys():
                    vocales[t] = 1 
                else:
                    vocales[t] += 1 
            
        maxVocal = max(vocales.values())
        for k,v in vocales.items():
            if maxVocal == v:
                window['salida'].update(f'La vocal que mas se repite es "{k}" {v} veces')
    
        
        

window.close()