#Hacer una clase Persona con dos métodos: uno para saber si es mayor de edad 
# y el otro para determinar si es varón o mujer. 
# En el programa principal instanciarlo, tomar nombre, edad y sexo, 
# y finalmente mostrar un cartel que diga 
# por ejemplo ‘Juan es mayor de edad y es varón’.

class Persona():
    def __init__(self,name,age,gen):
        self.name = name
        self.age = age
        self.gen = gen
    
    def edad (self):
        return self.age
        
    def genero (self):              
        return self.gen
                    
if __name__ == '__main__':
    lPersonas = []

    p1 = Persona('Jose',19,'m')
    p2 = Persona('Helena',22,'f')
    p3 = Persona('Mariano',14,'m')
    p4 = Persona('Pedro',124,'m')
    
    lPersonas.append(p1)
    lPersonas.append(p2)
    lPersonas.append(p3)
    lPersonas.append(p4)

    for e in lPersonas:
        if e.edad() >= 18:
            if e.genero() == 'm':
                print(e.name,'es mayor de edad y es varon.')
            else:
                print(e.name,'es mayor de edad y es mujer.')