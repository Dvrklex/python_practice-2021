
#  Motor: con métodos para arrancar el motor y apagarlo. 


class Motor():

    def arrancar(self): 
        self.motor = 'Encendido'
        return self.motor 
        
    def apagarlo(self): 
        self.motor ='Apagado'
        return self.motor  