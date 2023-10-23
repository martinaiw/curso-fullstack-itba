class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo)
        self.color = color
        self.puertas = puertas
        
    def ajustar_respaldo(self):
        print("Ajustamos el respaldo.")
        
    def subir_ventanilla(self):
        print("Subimos la ventanilla.")
        
    def __str__(self):
        return f"Tu vehículo es un {self.marca} {self.modelo}, color {self.color}, con {self.puertas} puertas"
        
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cc):
        super().__init__(marca, modelo)
        self.cc = cc
        self.color = color
    
    def bajar_patita(self):
        print("Bajamos la patita.")
        
    def hacer_ruido_grone(self):
        print("Hacemos ruido grone brrrm brrrmmmmmmmmmm.")
        
    def __str__(self):
        return f"Tu vehículo es una {self.marca} {self.modelo}, color {self.color}, con {self.cc} cc"
        
moto1 = Moto("Yamaha", "YZF-R6", "azul", 599)
auto1 = Coche("Ford", "Ka", "plateado", 3)

print(moto1)
print(auto1)
moto1.hacer_ruido_grone()
auto1.subir_ventanilla()