# input con opciones (Ejemplo: ‘Quiere ingresar datos (si/no)”?)


def inputChoise (mensaje,**kwargs):    
    validado = False
    while not validado: 
        for key,value in kwargs.items():
            print('>>',key,'= ',value)
        ops = input(mensaje)
        for buscar in kwargs.keys(): 
            if ops == buscar:
                print(kwargs[ops])
                validado = True
            
                


if __name__ == '__main__':
    # prueba1 = inputChoise('Eliga una opcion: ',color1 = 'Rojo', color2 = 'Azul',color3 = 'Negro')
    # q = inputChoise('¿Haces deportes? \n', uno= 'Si', dos= 'No',tres='Aveces',cuatro = 'Nunca')
    # datos = inputChoise('¿Quiere ingresar datos? ', Si = 'Empezemos...',No = 'Nos vemos...' )
    # prueba3 = inputChoise('eliga la pieza del tablero que quiera mover:',p1='avanza el peon',p2='mueves el caballo',p3='se mueve el alfil',p4='mueve la torre',p5='mueve la dama',p6='mueve el rey',checkmate='ganas por jaquemate',enroque='enroque torre y rey')
