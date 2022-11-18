#ontar la cantidad de palabras.
#texto: “Quiero comer manzanas, solamente manzanas.”


def contarPalabras (palabras):
    wordCount  = 0
    for i in range (len(palabras)):
        if palabras[i] != ' ' and palabras[i] != ',' and palabras[i] != '.':
            wordCount = wordCount + 1
    return wordCount
txt = 'Quiero comer manzanas, solamente manzanas.'
texto = txt.split()
print('La cantidad de palabras del texto es: ',contarPalabras(texto))