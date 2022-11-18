import PySimpleGUI as sg

layout = [ 
            [sg.Text('Ingrese nombre')],
            [sg.Input(key='nombre')],
            [sg.Text(size=(40,1),key='salida')],
            [sg.Button('Saludar'),sg.Button('Reirse'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) #winTitle = titulo de la ventana

while True:
    event, values = window.read() 
    print('Event:', event,type(event))
    print('Values:',values,type(event))
    if event in [None, 'Exit']:
        break
    if event == 'Saludar':
        window['salida'].update(f'Que peruano {values["nombre"]} que sooos')
    elif event == 'Reirse':
        window['salida'].update('Tenes un ranciometro')
    

window.close()