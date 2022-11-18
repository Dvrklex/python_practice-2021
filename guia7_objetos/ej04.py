#Definir una clase Persona cuyo constructor reciba nombre y edad. 
#El programa principal pedirá en forma repetitiva (hasta que no haya más) los mismos datos, 
#hará la instanciación de un objeto y lo agregará en una lista.
#Por lo tanto, los elementos de dicha lista serán objetos y 
#podrá mostrarse por recorrido y/o por subindicación
from fuimba import inputInt
class Person():
    def __init__(self,name, age):
        self.name = name 
        self.age = age
        
if __name__ == '__main__':
    q = 's'
    lis = []
    while q == 's':
        nombre = input('Ingrese nombre: ')
        edad = inputInt('Ingrese edad: ')
        persona = Person(nombre, edad)
        lis.append(persona)
        print('>> Persona agregada.')
        q = input('Agregar mas personas? (s/n): ')
    for personas in lis:
        print(personas.name, personas.age)