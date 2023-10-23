class Estudiante:
    def __init__(self, nombre, edad, materias_aprobadas):
        self.nombre = nombre
        self.edad = edad
        self.materias_aprobadas = materias_aprobadas
          
    def agregar_materia(self, materia):
        self.materias_aprobadas.append(materia)
        return print("Materia agregada exitosamente!")
    
    def __del__(self):
        print(f"Es una pena verte ir {self.nombre}, hasta la proxima!")
        self.nombre = None
        self.edad = None
        self.materias_aprobadas = None
        
alumno1 = Estudiante("Martina", 20, ["Algebra","Analisis Matematico", "Algoritmos2"])
alumno1.agregar_materia("Sistemas Operativos")