#Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. 
# Instanciar en  el programa principal (una sola línea en total). 
# La salida debe ser por ejemplo: Auto: VW Modelo: Gol

class Auto():
    def __init__(self,marca,año):
        self.marca = marca 
        self.año = año 
    def getData (self):
        pass

class Marca(Auto):
    modelo = None
    def getData (self):   
        return f'Auto: {self.marca} ,Marca: {self.modelo}'

if __name__ == '__main__':
    a1 = Marca('VW',2010)
    a1.modelo = 'Gol'
    datosA1 = a1.getData()
    print(datosA1)
