class Automovil:
    
    #Creamos metodo constructor
    def __init__(self, aa, pl, col, mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    #metodos
    def encender(self):
        print('encender' + self.marca)
    
    def avanzar(self):
        print('encender' + self.marca)
    
    def acelerar(self):
        print('encender' + self.marca)
    
    def frenar(self):
        print('encender' + self.marca)


##Creamos Objetos
vw= Automovil(1970,'CH-1234','Amarillo','Volkswagen')
vw.encender()
vw.acelerar()
vw.frenar()

tico = Automovil(1985,'EJ-234','Rojo','DAEWOO')
tico.encender()
tico.acelerar()
tico.frenar()