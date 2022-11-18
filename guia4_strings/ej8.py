#Contar la cantidad de letras (no incluir los separadores).
txt = 'Quiero comer manzanas, solamente manzanas.'

c = 0       #Acumulador de letras totales.
for i in txt:       #Contador de letras.
    if i != ' ' and i != ',' and i != '.':
        c  += 1     #Si es una letra le suma uno al acumulador 'c'.

print('La cantidad de letras en la frase es: ',c)