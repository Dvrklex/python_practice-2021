#Usando las clases Operacion y Suma, definir otra que se llame Promedio y utilizarla.
from fuimba import inputInt
class Operacion ():
    def tomaDatos(self):
        self.numeros = []
        condicion = 'si'
        while condicion == 'si':
            self.numeros.append(inputInt('Ingrese un numero: '))
            condicion = input('Desea agregar mas numeros? (si/no):')
    def opera(self):
        self.promedio = None
        
    def muestraResultado(self):
        print(self.promedio)
    
class Suma(Operacion):
    def opera (self):
        self.resuSuma = sum(self.numeros)

class Promedio(Operacion):
    def opera(self):
        self.resu = sum(self.numeros)
        self.promedio = self.resu // len(self.numeros)
        
    
if __name__=='__main__':

    s = Promedio()
    s.tomaDatos()
    s.opera()
    s.muestraResultado()


