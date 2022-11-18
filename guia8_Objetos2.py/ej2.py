
from fuimba import valInt,backTomenu,makeMenu
class Cafetera():
    def __init__(self,capActual):
        self.capActual = capActual        
    def llenarCafetera(self):
        self.capActual = 1000
        return self.capActual
    def servirTaza(self):#int
        self.cantTaza = valInt('Ingrese cantidad a servir: ',min = 0,max = self.capActual+1)
        self.capActual = self.capActual-self.cantTaza
        return self.capActual,self.cantTaza
    def vaciarCafetera(self):
        self.capActual = 0
        return self.capActual
    def mostrarCafetera(self):
        return self.capActual



if __name__ == '__main__':
    capacidadActual = valInt('Ingrese cantidad de cafe(0-1000): ',min=0,max=1000)
    cafeterra = Cafetera(capacidadActual)
    val = False
    while not val:
        makeMenu(op1= 'Ver capacidad actual de la cafetera.',op2='Vaciar cafetera.',op3='Llenar cafetera',op4='Servir taza de cafe.')
        print('0> Salir.')
        print()
        op = valInt('Ingrese opcion: ',min=-1,max= 5)
        print()
        if op == 1:
            cantAcutal = cafeterra.mostrarCafetera()
            print(f'La cantidad actual de la cafetera es {cantAcutal} ml.')
            backTomenu()
        elif op == 2:
            vacCafetera = cafeterra.vaciarCafetera()
            print('Se ha vaciacio la cafetera.')
            print(f'Cantidad actual {vacCafetera} ml.')
            backTomenu()
        elif op == 3:
            llenoCafetera =cafeterra.llenarCafetera()
            print('Se ha llenado la cafetera.')
            print(f'Cantidad actual {llenoCafetera} ml.')
            backTomenu()
        elif op == 4:
            messirve,cantRestante = cafeterra.servirTaza()
            print(f'Cantidad de la taza servida {messirve} ml.')
            print(f'Cantidad actual de la cafetera {cantRestante} ml')

            backTomenu()
        else:
            val = True 













