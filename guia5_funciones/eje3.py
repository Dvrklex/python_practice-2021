#Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes).
#texto: “Quiero comer manzanas, solamente manzanas.”



def contarLetras (letras):
    countWord = 0    
    for i in letras:       
        if i != ' ' and i != ',' and i != '.':
            countWord = countWord + 1                
    return countWord               
txt = 'Quiero comer manzanas, solamente manzanas.'
print('La cantidad de letras es',contarLetras(txt))

