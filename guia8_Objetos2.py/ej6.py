from fuimba import *
import random
class VideoClub():
    def __init__(self):
        self.listaPeliculas = [
                ['Dont Breathe 2',500,10,'no','Suspenso',2021,'Rodo Sayagues','Stephen Lang'],
                ['Luca',300,7,'si','Aventura',2021,'Enrico Casarosa','Jabob Tremblay'],
                ["KickAss",300,7,"si","comedia",2010,"Matthew Vaughn","aaron taylor-johnson"],
                ['Space Jam',501,9,'no','Comedia',2021,'Malcolm Lee','Lebron James']
                ]       
        self.listaClientes = [
            [12,'Peruano','Martin San 145','3584687911',7],
            [1,'roberto carlos','maipu 1151','03456456754',3],
            [2,'mirtha viejan','buenos aires 809','0346785347',7]
            ]
        self.lAlquileres = [['Peruano','Luca','03/11/2021','10/11/2021',300]]
class Producto(VideoClub):
    def listaProductos(self):
        print('Peliculas disponibles: ')        
        for lista in self.listaPeliculas:
            nombre,costo,diasAlq,estado,genero,anio,director,actores= lista
            print(f'> {nombre}')    
            
    def añadirProducto (self):
        self.newProducto = []
        nombre = input('Nombre de la pelicula: ')
        self.newProducto.append(nombre)
        precio = inputInt('Precio del producto: ')
        self.newProducto.append(precio)
        cantDias = inputInt('Cantidad de dias de alquiler: ')
        self.newProducto.append(cantDias)
        estado = 'no'
        self.newProducto.append(estado)
        genero = input('Ingrese genero: ')
        self.newProducto.append(genero)
        fecha = inputInt('Fecha de estreno: ')
        self.newProducto.append(fecha)
        dire = input('Director: ')
        self.newProducto.append(dire)
        protagonista = input('Actor principal: ')
        self.newProducto.append(protagonista)
        self.listaPeliculas.append(self.newProducto)

    def fichaProductos(self):
        print('Ficha de productos: ')      
        print()
        print(' Nombre - Costo - Dias de Alquiler - Estado - Genero - Año - Director - Protagonista')  
        for lista in self.listaPeliculas:
            nombre,costo,diasAlq,estado,genero,anio,director,prota= lista
            print(f'> {nombre}  -  {costo}  -  {diasAlq}  -  {estado}  -  {genero}  -  {anio}  -  {director}  - {prota}')    
                    

class Cliente(VideoClub):   
    def listadoClientes(self):# Nº cliente, nombre, dirección, teléfono, productos alquilados
        print('Listado de clientes: ')
        print()
        print(f'Nº Cliente - Nombre - Direccion - Celular - Cantidad Pelicuals Alquiladas')
        for cliente in self.listaClientes:
            numCliente,nombre,direccion,cel,cPelAlq = cliente
            print(f'Nº{numCliente}>  {nombre} - {direccion} - {cel} - {cPelAlq}')

    def añadirCliente(self):
        self.newCliente = []
        numCliente = int(random.randint(0,30)) 
        self.newCliente.append(numCliente)
        nombre = input('Ingrese nombre del cliente: ')
        self.newCliente.append(nombre)
        direccion = input('Direccion del cliente: ')
        self.newCliente.append(direccion)
        telefono = input('Numero de telefono: ')
        self.newCliente.append(telefono)
        productosAlquilados = 0
        self.newCliente.append(productosAlquilados)
        self.listaClientes.append(self.newCliente)

class Alquiler(VideoClub):
    def fichaCliente(self):
        print('Fichas de  Clientes: ')
        print()
        print('Nombre  -  Pelicula  -  Fecha Alquiler - Fecha Devolucion -  Monto')
        for ficha in self.lAlquileres:
            nombre,pelicula,diaAlq,diaDev,monto = ficha
            print(f'{nombre} - {pelicula} - {diaAlq} - {diaDev} - {monto}')

    def alquilarProductos(self):
        self.listaNuevaAlquiler = []
        self.listaAlq = []
        self.listaPrecioAlq = []
        for x in self.listaPeliculas:
            titulo,precio,plazo,disponibilidad,genero,año,director,actor = x
            #print("-",titulo)
            self.listaAlq.append(titulo)
            self.listaPrecioAlq.append(precio)
        print("Alquiler De Peliculas")    
        for x in range (len(self.listaAlq)):     
            print(x ,"-",self.listaAlq[x],"--->",self.listaPrecioAlq[x])
        

        cod_Pelicula = valInt("ingrese codigo de la pelicula: ",min = -1 , max = len(self.listaAlq) + 1)
        for x in range (len(self.listaAlq)):
            if cod_Pelicula == x:
                print(f'Ha seleccionado {self.listaAlq[cod_Pelicula]} - ${self.listaPrecioAlq[x]}') 

       
        nombre = input("Ingrese su nombre: ")
        self.listaNuevaAlquiler.append(nombre)
        self.listaNuevaAlquiler.append(self.listaAlq[cod_Pelicula])
        plazo = input("Ingrese fecha de alquiler: ")
        self.listaNuevaAlquiler.append(plazo)
        devolucion = input("Ingrese fecha de devolucion: ")
        self.listaNuevaAlquiler.append(devolucion)
        self.listaNuevaAlquiler.append(self.listaPrecioAlq[cod_Pelicula])
        self.lAlquileres.append(self.listaNuevaAlquiler)
        


class App():
    def __init__(self):
        self.val = True
        prod = Producto()
        cli = Cliente()
        alq = Alquiler()

        while self.val == True: 
            print('    >Menu<')
            makeMenu(uno = 'Lista de productos.',dos='Añadir productos.',tres='Ficha de productos.',cuatro='Lista de clientes.',cinco='Añadir Cliente.',seis='Ficha de cliente.',siete='Alquiler de productos.')
            print('0> Salir.')
            opMenu = valInt('> Ingrese opcion: ',min=-1,max=8)
            if opMenu == 1: #ver listas de peliculas
                prod.listaProductos()
                subrayar()
                backTomenu()                
            elif opMenu == 2:#añadir producto
                prod.añadirProducto()
                subrayar()
                backTomenu()
            elif opMenu == 3: #ficha de los productos
                prod.fichaProductos()
                subrayar()
                backTomenu()
            elif opMenu == 4: #listado de los clientes cargados
                cli.listadoClientes()
                subrayar()
                backTomenu()
            elif opMenu == 5:#añadir cliente
                cli.añadirCliente()
                subrayar()
                backTomenu()
            elif opMenu == 6:#ver los alquileres activos 
                alq.fichaCliente()
                subrayar()
                backTomenu()
            elif opMenu == 7:
                alq.alquilarProductos()
            elif  opMenu == 0:
                print('Esta seguro de salir?')
                print('1=Si | 2=No')
                salir = valInt('Opcion: ',min=0,max=3)
                if salir == 1:    
                    self.val = False
                
    
a = App()