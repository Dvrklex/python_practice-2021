# Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
# 
#
import PySimpleGUI as sg
from fuimba import  verificarInt

layout = [
            [sg.Text('Seleccione dia')],
            [sg.Radio('Lunes','DIA1',key='lunes'),sg.Radio('Martes','DIA1',key='martes'),sg.Radio('Miercoles','DIA1',key='miercoles'),sg.Radio('Jueves','DIA1',key='jueves')],
            [sg.Radio('Viernes','DIA1',key='viernes'),sg.Radio('Sabado','DIA1',key='sabado'),sg.Radio('Domingo','DIA1',key='domimgo')],
            [sg.Text('ML'),sg.Input(key='mldia')],
            [sg.Button('Cargar'),sg.Button('Total'),sg.Button('Dia mas llovido'), sg.Button('Salir')]
            ]

window = sg.Window('MEDIDOR DE LLUVIA', layout) 

lluvia = {}
total = 0

while True:
    event, values = window.read()
    if event in [None, 'Salir']:
        break
    if event == 'Cargar':
        verificar = verificarInt(values['mldia'])
        if verificar[0] == False:
            sg.popup('Los milimetros ingresados no son validos.')
        else:
            for k,v in values.items(): 
                if v == True:
                    if k not in lluvia:
                        lluvia[k] = verificar[1]
                        window['mldia'].update('')
                    else: 
                        sg.popup('No puedes cargar dos veces el mismo dia.')
    elif event == 'Total':
        for valor in lluvia.values(): 
            total+=valor
        sg.popup('Total llovido:',f'> {total} ml')
        total = 0
    elif event == 'Dia mas llovido':
        diasMasLLovido = ''
        masLluvia = max(lluvia.values())
        for k,v in lluvia.items():
            if masLluvia == v:
                diasMasLLovido += k.capitalize() + ' - ' +str(v) + ' mls' + '\n'
        sg.popup('El dia mas llovido',diasMasLLovido)

window.close()

