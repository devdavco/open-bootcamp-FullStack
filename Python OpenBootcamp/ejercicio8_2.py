import pickle

class Vehiculo():
    marca = ''
    color = ''
    velocidad = 0

    def __init__(self,marca,color,velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color

    def getVelocidad(self):
        return self.velocidad


miCarro = Vehiculo('Tesla','Azul',250)



with open('datos.bin','wb') as f:
    pickle.dump(miCarro,f)


with open('datos.bin','rb') as f:

    recuperar_carro = pickle.load(f)

print(recuperar_carro.getColor())

