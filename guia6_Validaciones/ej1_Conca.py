#Concatenar un número indeterminado de strings con un caracter determinado 
#(por defecto un espacio)


def concatenar (*args,sep=' '):
    salida = ''
    for e in args:
        salida += e + sep
    return salida[:-1]
if __name__ =='__main__':
    print(concatenar('hola','como','andas','todo','bien','?'))
    print(concatenar('1','2','3','4',sep=' '))


# ---Ejemplo Pablo Kan---
# def conca (*args,sep=' '):
#     return sep.join(args)

