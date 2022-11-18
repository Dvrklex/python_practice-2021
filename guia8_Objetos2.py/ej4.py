
class Cancion():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def dameTitulo(self): 
        return self.titulo
    
    def dameAutor(self):
        return self.autor
    def ponerTitulo(self):
        self.establecerTitulo = input('Establezca un nuevo titulo: ')
        self.titulo = self.establecerTitulo 
        return self.titulo
    def ponerAutor(self):
        self.establecerAutor = input('Establezca un nuevo autor: ')
        self.autor = self.establecerAutor 
        return self.autor

if __name__ == '__main__':
    c1 = Cancion('Runaway','Bon Jovi')
    titulo = c1.dameTitulo()
    autor = c1.dameAutor()
    print(f'El titulo de la cancion es {titulo}.')
    print(f'El autor de la cancion es {autor}')
    camTitulo = c1.ponerTitulo()
    camAutor = c1.ponerAutor()
    print(f'El nuevo titulo es {camTitulo}')
    print(f'El autor de la cancion es {camAutor}')
