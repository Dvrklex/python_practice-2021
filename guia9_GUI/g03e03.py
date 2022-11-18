# Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
# Recorrerlas y mostrar los nombres de las mujeres. 
import PySimpleGUI as sg

layout = [
            
            [sg.Text('Nombre'), sg.Input(key='nombre')],
            [sg.Radio('Masculino','SEXO1',default=False,key='mas'),sg.Radio('Femenino','SEXO1',default = True,key='fem')],
            [sg.Text(size=(40,1),key='mostrar')],
            [sg.Button('Cargar'),sg.Button('Mostrar'), sg.Button('Exit')]
            ]

window = sg.Window('Listas paralelas', layout)

lNombres = []
lGen = []
while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    if event == 'Cargar':
        if values['fem'] == True:
            name = values['nombre']
            gen = 'f'
            lNombres.append(name)
            lGen.append(gen)
        else:
            name = values['nombre']
            gen = 'm'
            lNombres.append(name)
            lGen.append(gen)
        
    elif event == 'Mostrar':
        muj =''
        for mujeres in range(len(lGen)):
            if lGen[mujeres] == 'f':
                muj +=  lNombres[mujeres] + '\n'
        sg.popup('Lista de mujeres',muj)
window.close()