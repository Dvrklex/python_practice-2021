#Guardar en una lista los números pares mayores que 0 y menores que 31. 

listaNumeros = []   
for i in range (1,32):
    if i%2 == 0 :
        listaNumeros.append(i)

print('Estos son los numeros pares mayores a 0 y menores a 31', listaNumeros)
    
    




listaNumeros = [int(i) for i in range(1,32) if i%2 == 0]
print('Lista por comprension',listaNumeros)






    
    
    