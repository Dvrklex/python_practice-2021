#Transformar la cadena "River vuelve a las copas", en la cadena "River vuelve a la copa".
# Resolverlo recorriendo la cadena original como si fuera una lista.

r1 = 'River vuelve a las copas'
t = ''
for i in range (len(r1)):
    if r1[i] != 's':
        t == t + r1[i]

print(t)












