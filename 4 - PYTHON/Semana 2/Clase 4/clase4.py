class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def conducir(self):
        print("El vehiculo está en movimiento.")
    def acelerar(self):
        print("Estamos acelerando.")
    def estacionar(self):
        print("El vehículo está estacionado.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
    def conducir(self):
        print(f"El coche {self.marca} {self.modelo} de color {self.color} está en movimiento.")
    def estacionar(self):
        print("El coche está estacionado.")
        
        
class Moto(Vehiculo):
    def frenando(self):
        print("Estamos frenando.")
        
coche = Coche("Ford", "Mustang","rojo")
moto = Moto("Honda", "CBR")

coche.conducir()
moto.conducir()
moto.acelerar()
moto.frenando()
coche.estacionar()
moto.estacionar()



