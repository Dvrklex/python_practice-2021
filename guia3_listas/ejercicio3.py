#Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
# Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
#Mostrar los elementos de la lista resultante.
# 1: Creacion y carga de listas
registro=[]
sexo=[]
for i in range(2):
    nombre=input('Ingrese un nombre: ')
    registro.append(nombre)
    es=input('Ingrese un sexo (M/F): ')
    sexo.append(es)

# 2: Recorrerlas y guardar los nombres de las mujeres en una nueva lista 
mujeres=[]
for i in range(2):
    if sexo[i]=='f':
        mujeres.append(registro[i])

# 3: Mostrar los elementos de la lista resultante
for i in range(len(mujeres)):
    print(mujeres[i])