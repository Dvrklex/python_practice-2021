# Crea las siguientes clases (cada una en su archivo): 
#  Rueda: con métodos para inflar la rueda y desinflarla. 
#  Ventana: con métodos para abrirla y cerrarla. 
#  Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
#  Coche: con un motor, cuatro ruedas y dos puertas;  
# con los métodos que te parezcan 
from motor import Motor
from rueda import Rueda 
from ventana import Ventana
from puerta import Puerta


class Coche(Motor,Rueda,Ventana,Puerta):
    def __init__(self,on,off): 
        self.on = on
        self.off = off
        
if __name__ == '__main__':
    miauto = Coche('on','off')
    print('Motor',miauto.arrancar())
    print('Puertas ',miauto.abrirPuerta())
    print('Ruedas',miauto.inflarRueda())
    print('Ventanas ',miauto.abrirVentana())
    print()
    print('Motor',miauto.apagarlo())
    print('Puertas ',miauto.cerrarPuerta())
    print('Ruedas',miauto.desinflarRueda())
    print('Ventanas ',miauto.cerrarVentana())