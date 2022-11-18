#Agregar al ejercicio 2 (clase Auto) un método que obtenga la antigüedad. 
# En el programa principal mostrar cuáles autos tienen más de 5 años.


class Auto():
    def __init__(self,marca,año):
        self.marca = marca 
        self.año = año 
    def getData (self):
        return 2021 - self.año
if __name__ == '__main__':   
    lAutos = []
    a1 = Auto('Ford', 1990)
    a2 = Auto('Toyota', 2018)
    a3 = Auto('Mustang', 2001)

    lAutos.append(a1)
    lAutos.append(a2)
    lAutos.append(a3)

    for auto in lAutos:
        if auto.getData() >= 5:
            print('Marca:',auto.marca,', Año:',auto.año)