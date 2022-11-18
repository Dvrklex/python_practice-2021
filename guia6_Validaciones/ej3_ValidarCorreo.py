#  Validar una dirección de correo electrónico
def emailVal (correo):
    error = '*Sonido de error* El correo ingresado no es válido.'
    validado = False
    while not validado: 
        dir = input(correo)
        try:
            if '@' and '.' in dir:
                aux  = dir.split('@')    
                usu = aux[0]
                resto = aux[1]
                aux2= resto.split('.')
                dominio = aux2[0]
                terminacion = aux2[1]
                if (usu.isalpha() == True) or (usu.isalnum() == True) or  (usu.isascii() == True and ' ' not in usu):    
                    if (dominio.isalpha() == True) and (terminacion.isalpha() == True):
                        validado=True
                        print('Dirección de correo válida.')
                    else:
                        print(f'{error}')            
                else:
                    print(f'{error}')            
            else:
                print(f'{error}')            
        except: 
            print(f'{error}')            

if __name__ == '__main__':
    email = emailVal('Ingrese correo electronico: ')