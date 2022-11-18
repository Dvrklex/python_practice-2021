#Definir una clase que al ser instanciada reciba un valor numérico y 
# cargue una lista de nombres hasta esa cantidad. 
# Hacer también un método que muestre la lista completa.

class CargaPersonas():
    def __init__ (self,cantidad):
        self.names= []
        for add in range(cantidad):
            self.names.append(input('> Ingrese un nombre: '))

    def getData (self):
        return self.names


if __name__ == '__main__':
    cant1  = CargaPersonas(4)
    listaP1 = cant1.getData()
    print(listaP1)