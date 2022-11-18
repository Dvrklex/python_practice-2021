#  Crea una clase Cuenta (bancaria) con atributos para el número de cuenta, 
# el DNI del cliente, 
# el saldo actual y 
# el interés anual que se aplica a la cuenta (porcentaje). 
# ----------------------------------------------------------
# Define en la clase los siguientes métodos: 
# constructor con DNI, saldo e interés. 
# Método actualizarSaldo(): actualizará el saldo de la cuenta
# aplicándole el interés diario 
# (interés anual dividido entre 365 aplicado al saldo actual), 
# --------------------------------------------------------------
# método ingresar(float):  permitirá ingresar una cantidad en la cuenta, 
# método retirar(float): permitirá sacar una cantidad de la cuenta (si hay saldo).
# 
#  Finalmente, un método que nos permita mostrar todos los datos de la cuenta. 


from fuimba import inputFloat,inputInt

class Cuenta():#bancaria
    numCuenta = None
    def __init__ (self,DNI,saldo,interes):       
        self.DNI = DNI
        self.saldo = saldo
        self.interes = interes

    def actualizarSaldo(self):
        self.intDiario = self.interes / 365
        return self.saldo*self.intDiario

    def ingresarSaldo(self):       
        addSaldo = inputFloat('Ingrese saldo: ')
        return self.saldo + addSaldo

    def retirarSaldo(self):
        removeSaldo = inputFloat('Ingrese saldo a retirar: ')
        return self.saldo - removeSaldo

    def showDatos(self):
        return self.DNI,self.saldo,self.interes


if __name__ == '__main__':
    # cuenta = inputInt('Ingrese Nº cuenta: ')
    # dni = inputInt('Ingrese DNI: ')
    # saldo  = inputFloat('Ingrese saldo actual de la cuenta: ')
    # interes = inputFloat('Ingrese interes anual: ')
    cuenta = '1644168091'
    dni = '40.489.120'
    saldo = 39489.89
    interes = 22.9
    persona = Cuenta(dni,saldo,interes)
    persona.numCuenta=cuenta
    valid = False
    while not valid:
        print('1.Ver saldo de la cuenta.')
        print('2.Agregar saldo a la cuenta.')
        print('3.Retirar saldo de la cuenta.')
        print('0.Salir')
        preg = inputInt('> Ingrese opcion: ')
        if preg == 1: 
            print(f'Saldo de la cuenta: ${saldo}')
        elif preg == 2:
            persona.ingresarSaldo()
        elif preg == 3:   
            persona.retirarSaldo()
        elif preg == 0:
            valid = True
        else: 
            print('Opcion invalida.')
    d,sal,inte = persona.showDatos()

    print(f'Nº cuenta: {persona.numCuenta}')
    print(f'DNI del titular: {d}')
    print(f'Saldo de la cuenta: ${saldo}')
    print(f'Interes diario: {inte}')
