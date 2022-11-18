#Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python".
#  Cortar la cadena original, agregarle el literal "Programación en" y concatenar.


from typing import Text


curso = 'Curso de Python'
txt = curso.split()
txt.insert(2,'Programacion')
txt.insert(3,'en')
print(txt)
frase = ' '.join(txt)      #Pasar una lista a str
print(frase)  