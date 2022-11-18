#Almacenar en dos  listas paralelas, nombres y sexos de 8 personas.
#Al finalizar, recorrerlas y mostrar los nombres de las mujeres.
#Dos funciones: carga y mostrarMujeres


def carga():
    nomb = []
    sex = []
    for x in range(1,8):
        nombres = input('Ingrese el nombre: ')
        sexo = input('Ingrese el sexo: (H/M) ')
        nomb.append(nombres)
        sex.append(sexo)
    return nomb,sex
nombres = carga()
n = nombres[0]
s = nombres[1]

def mostrarMujeres(nomb,sex):
    nombMujer = []
    for x in range(len(sex)):
        if sex[x] == 'M':
            nombMujer.append(nomb[x])

    return nombMujer

nombresMujeres = mostrarMujeres(n,s)
print('El nombre de las mujeres son: ',nombresMujeres)
            
