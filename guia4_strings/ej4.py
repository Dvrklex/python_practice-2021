# Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia
#  (googlear la tabla y las funciones de conversión en Python).

c=input("Ingrese caracter en minusculas: ")
if c>='a' and c<='z':
    c=chr(ord(c)-ord('a')+ord('A'))
print("En mayuscula es: {}".format(c)) 


t=input("Ingrese caracter en minusculas: ")
if t>='a' and t<='z':
    t=chr(ord(t)-ord('a')+ord('A'))
print("En mayuscula es: {}".format(t)) 

f=input("Ingrese caracter en minusculas: ")
if f>='a' and f<='z':
    f=chr(ord(f)-ord('a')+ord('A'))
print("En mayuscula es: {}".format(f))

palabra = (c + t + f)

print(palabra)


# buscar posicion en ascii 

import string

minusculas = string.ascii_lowercase   # O si prefieres pones "abcde...z" que es lo mismo
mayusculas = string.ascii_uppercase   # "ABCDE...Z"

def letra_a_codigo(letra):
   if letra in minusculas:
       return minusculas.index(letra) + 97
   if letra in mayusculas:
       return mayusculas.index(letra) + 65

print(letra_a_codigo('j'))
# Resultado: 106








