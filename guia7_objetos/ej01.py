#hacer una clase telefono con los atributos marca, modelo y costo mensual 
# y un metodo que muestre o devuelva el costo anual

class Telefono():
    def setData (self,marca,modelo,costoM):
        self.costoM = costoM
        self.marca = marca
        self.modelo = modelo
           
    def getData (self):
        return self.marca,self.costoM * 12

if __name__ == '__main__':
    telefono1 =  Telefono()
    telefono2 = Telefono()
    telefono1.setData('MOtoRol4','XD 02',200)
    telefono2.setData('Jiaomy','Pokeria',400)
    mod1,costoTel1 = telefono1.getData()
    mod2,costoTel2 = telefono2.getData()

    print('Costo anual del',mod1,'es:',costoTel1) #Costo del MOtoRol4
    print('Costo anual del',mod2,'es:',costoTel2) #Costo del Jiaomy

