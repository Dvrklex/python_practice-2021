#En los siguientes ejercicios (6 a 11) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”,
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
# (los caracteres separadores son el espacio, la coma y el punto).


#Buscar una palabra completa en un texto y contar cuántas veces está.

texto = 'Quiero comer manzanas, solamente manzanas.'
print(texto)
buscador = str(input('¿Que palabras quiere buscar en el texto? '))
c = texto.count(buscador)

print('La cantidad de veces que se repite "',buscador,'" es', c)