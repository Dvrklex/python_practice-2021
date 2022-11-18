# Determinar cuál es la vocal que aparece con mayor frecuencia.


txt = 'Quiero comer manzanas, solamente manzanas.'

a = 0
e = 0
i = 0       #Variables que acumulan la cant de veces que aporece aparece una vocal
o = 0
u = 0 
#Acumula cuantas veces aparece cada vocal
for x in txt:
    if x == 'a':
        a = a +1 
    elif x == 'e':
        e = e+1
    elif x == 'i':
        i = i+1
    elif x == 'o':
        o = o+1
    elif x == 'u':
        u = u+1
#Compara cual es la vocal que aparece con mas frecuencia.
if a > e and a > i and a > o and a > u:
    c = 'a'
elif e > a and e > i and e > o and e > u:
    c = 'e'
elif o > a and o > e and o > i and o > u:
    c = 'o'
elif i > a and i > e and i > o and i > u:
    c = 'i'
elif u > a and u > e and u > o and e > i:
    c = 'u'
        
print('La vocal con mas frecuencia es la letra "',c,'"')               
         