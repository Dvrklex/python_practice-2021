#Redefinir la clase auto con los atributos marca, modelo y año. 
#Hacer una clase heredera TuAuto que agrega dueño y color. 
#Hacer un método que devuelve el color y en el programa principal 
# preguntar por un color y mostrar sólo los autos que cumplan esa condición.


class Auto():
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

class TuAuto(Auto):
    def __init__(self, marca, modelo, anio, duenio, color):
        Auto.__init__(self, marca, modelo, anio)
        self.duenio = duenio
        self.color = color

    def getColor(self):
        return self.color

if __name__ == '__main__':
    lAutos = []
    a1 = TuAuto('Ford','Mustang',2019,'A Rosales','Negro')
    a2 = TuAuto('Chevrolet','Aveo',2018,'Peruano','Gris')
    a3 = TuAuto('Nizzan','Choto',1999,'Chileno','Blanco')
    lAutos.append(a1)
    lAutos.append(a2)
    lAutos.append(a3)
    colorUsu = input('Ingrese un color: ')
    for color in lAutos:
        if colorUsu.capitalize() == color.getColor():
            print('Marca:',color.marca,'Modelo:',color.modelo,',Color:',color.color)

