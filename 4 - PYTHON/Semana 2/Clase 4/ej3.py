class Casa:
    def __init__(self, direccion, habitaciones):
        self.direccion = direccion
        self.habitaciones = habitaciones
    
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Familia(Casa, Persona):
    def __init__(self, direccion, habitaciones):
        self.casa = Casa(direccion, habitaciones)
        self.miembros = []
        
    def agregar_persona(self, nombre, edad):
        persona = Persona(nombre, edad)
        self.miembros.append(persona)
        
    def mostrar_informacion(self):
        print(f"Dirección de la casa: {self.casa.direccion}")
        print(f"Cantidad de habitaciones: {self.casa.habitaciones}")
        print("Miembros de la familia:")
        for persona in self.miembros:
            print(f"Nombre: {persona.nombre}, Edad: {persona.edad}")


familia1 = Familia("123 Calle Principal", 3)
familia1.agregar_persona("Juan", 35)
familia1.agregar_persona("Maria", 30)
familia1.agregar_persona("Pedro", 10)

familia1.mostrar_informacion()