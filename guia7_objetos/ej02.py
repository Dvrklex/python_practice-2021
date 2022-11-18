#definir una clase auto con un metodo que le permita poner la marca y el año. 
# En el programa principal declarar tres instancias (objetos),
# cargarlas y mostras las marcas de los 3 autos
class Auto():
    def __init__(self,marca,año):
        self.marca = marca 
        self.año = año 
    def getData (self):
        return self.marca, self.año

if __name__ == '__main__':
    auto1 = Auto('peuyot',2001)
    auto2 = Auto('nizan',2015)
    auto3 = Auto('Toyota',8470)

    p,a = auto1.getData()
    print('Marca:',p,' Año:',a)

