#Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
#  Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

s = 'Quiero comer manzanas, solamente manzanas.'
vieja = 'manzanas'
nueva = 'peras'
posi = 0
while posi != -1:
    posi = s.find(vieja)
    if posi != -1:
        inicio = s[:posi]
        final = s[posi+len(vieja):]
        s = inicio + nueva + final
print(s)