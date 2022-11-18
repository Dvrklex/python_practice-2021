#Definir una clase Telefono, sus atributos son: 
# marca, modelo, sistema operativo, plan(costo) y cantidad de RAM. 
# Sus métodos son: costo anual, 
# mostrar Sistema Operativo 
#y si es gama alta o no (con 6 o más gigas de RAM) .
from fuimba import inputInt

class Telefono ():
    def __init__(self,marca,modelo,sistemaOper,plan,ram):
        self.marca = marca
        self.modelo = modelo
        self.sistemaOper = sistemaOper
        self.plan = plan
        self.ram = ram

    def costoAnual(self):
        return self.plan * 12
    def mostrarSistemaOper (self):
        return self.sistemaOper
    def gama (self):
        if self.ram >= 6:
            return 'Alta'
        else:
            return 'Baja'
if __name__ == '__main__':
    marcaT = input('Ingrese marca: ')
    modeloT = input('Ingrese modelo: ')
    soT = input('Sistema operativo: ')
    planT = inputInt('Costo mensual: ')
    ramT = inputInt('Ingrese ram: ')
    t1 = Telefono(marcaT,modeloT,soT,planT,ramT)
    print('Sistema operativo:',t1.mostrarSistemaOper(),',Gama:',t1.gama(),',Costo anual:$',t1.costoAnual())
