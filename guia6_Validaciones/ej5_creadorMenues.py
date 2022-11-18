# def stop():
#     input('Enter para volver al menú')
 
#     def createUser():
#        print('función createUser')
#        stop()
 
#     def delUser():
#        print('función delUser')
#        stop()
 
#     def listUsers():
#        print('función listUsers')
#        stop()
 
#     menu(createUser='Crear usuario!', delUser='Borrar usuario', listUsers='Listar usuarios')
 
#     def foo():
#        print('foo')
#        stop()
# stop()
def makeMenu(**kwargs):
    lista = []
    lista.append(kwargs)
    c = 1
    for e in lista: 
        for valor in e.values():
            salida = str(c)+ '> ' + valor
            print(salida)
            c += 1
        




if __name__ == '__main__':
    makeMenu(createUser='Crear usuario!', delUser='Borrar usuario', listUsers='Listar usuarios')