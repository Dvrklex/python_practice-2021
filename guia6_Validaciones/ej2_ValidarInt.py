import sys
infinite = 1e309
def valInt (mensaje, min=-infinite, max=infinite): #validar rango de enteros
    validado = False
    while not validado: 
        num= input(mensaje)
        try:
            num= int(num)
            if num > min and num < max:
                validado = True
            else: 
                print('Error. Debe respetar el rango.')
        except:
            print('Error. Debe ingresar un numero Entero.')

def valFloat (mensaje, min=-infinite, max=infinite):#validar rango de float
    validado = False
    while not validado: 
        num= input(mensaje)
        try:
            num= float(num)
            if num > min and num < max:
                validado = True
            else: 
                print('Error. Debe respetar el rango.')
        except:
            print('Error. Debe ingresar un numero Decimal.')

if __name__ =='__main__':  
    # n = valInt('Ingrese un entero entre 3 y 7: ', 3, 7)
    # m = valInt('Cualquier entero: ')
    # maximo = valInt('Ingrese un entero menor a 1000: ', max=1000) 
    # minimo = valInt('Ingrese un entero mayor a 1000: ', min=1000)
    # negativo = valInt('Ingrese un numero negativo mayor a -1000: ', min = -1000)
    # negativo2 = valInt('Ingrese un numero negativo menor a -1000: ', min = -1000)
    
    # m = valFloat('Cualquier decimal: ')
    # maximo = valFloat('Ingrese un decimal menor a 1000: ', max=1000) 
    # minimo = valFloat('Ingrese un decimal mayor a 1000: ', min=1000)
    # negativo = valFloat('Ingrese un numero negativo mayor a -1000: ', min = -1000)
    # negativo2 = valFloat('Ingrese un numero negativo menor a -1000: ', min = -1000)