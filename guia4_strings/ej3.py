#Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.
print('------------------------------------------------------------------------------------------')
txt = 'Hola, como estas?. Cuanto tiempo estuviste fuera de la cuidad?. Estaras mucho tiempo aqui?'
print(txt)
print('------------------------------------------------------------------------------------------')
buscador = input('Coloque aqui la letra que quiere buscar en el texto anterior: ')
c  = txt.count(buscador)

print('La cantidad de veces que se repite la letra "',buscador,'" es', c)