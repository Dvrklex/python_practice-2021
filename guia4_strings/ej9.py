#Contar la cantidad de palabras.
txt = 'Quiero comer manzanas, solamente manzanas.'
texto = txt.split()
wordCount  = 0

for i in range (len(texto)):
    if texto[i] != ' ' and texto[i] != ',' and texto[i] != '.':
        wordCount = wordCount + 1


print('La cantidad de palabras del texto es: ',wordCount)