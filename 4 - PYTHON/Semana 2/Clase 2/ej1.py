class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    def ladrar(self):
        print("¡Guau, guau!")
        
        
perro = Perro("Berro", 3)
perro2 = Perro("Runipie", 0.4)
print(perro)
perro.ladrar()
print(perro2)