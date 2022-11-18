#Averiguar qué cantidad de letras tiene la palabra más larga y cual es.


txt = 'Quiero comer manzanas, solamente manzanas.'
l = txt.split()

palabraMasLarga = []
for p in l:
    if p != ' ' or p != ',' or p != '.':
        palabraMasLarga.append((len(p),p))
        palabraMasLarga.sort()

ml = palabraMasLarga[-1][1]
cantLetras = ml.count('')
print('La palabra mas larga es ',ml,' y tiene ',cantLetras - 1  ,' letras.')
 

    