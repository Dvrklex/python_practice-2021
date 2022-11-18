# input de strings (validar largo por mínimo y/o máximo)
   
def strVal_largo (str, min = 1):
    validado =  False
    error = 'La frase ingresada no respeta el limite.'
    while not validado:
        string = input(str)
        # print(len(string)) 
        if len(string) >= min:
            validado = True
        else: 
            print(f'{error}')



            
if __name__ == '__main__':  
    a = strVal_largo('Ingrese una frase: ', min = 10)
    b = strVal_largo('Ingrese cualquier letra: ')
 