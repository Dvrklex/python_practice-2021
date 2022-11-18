import PySimpleGUI as sg
# desde la consola pip install pysimplegui --- sino anda en la consola poner py m- pip install... y la libreria
# Ir a archivo,preferencias, fragmento de codigo de usuario o snippets, poner py, y copiar el python.json ahi
# sg.text es para poner textos
# sg.Input es para tomar datos 
# sg.Button son los botones
# entrar en pysimplegui.org y pysimplegui.com para ver la documentacion
# crear una carpeta PSG para los trabajos de interfaz y ahi meter las cosas de interfaz, guias, etc
layout = [ #layout es una convencion, podria llamarse fillas (es una lista de listas)
            [sg.Text('Ingrese nombre')],#cada una de estas listas es una fila de la ventana
            [sg.Input(key='nombre')], #la llave es para referenciar donde se guardo el valor
            [sg.Button('OK'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) #winTitle = titulo de la ventana

while True:
    event, values = window.read() #el event siempre devuelve una string, y el values devuelve siempre un diccionario
    #en los values, va a devolver en este caso la key que puse en el input y lo que haya escrito en esa caja
    #print('Event:', event,type(event))
    #print('Values:',values,type(event))
    if event in [None, 'Exit']:
        break
    

window.close()