class Figura:
    def calcular_area(self):
        pass
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura / 2
    def __str__(self):
        return f"El triángulo es de base {self.base} y altura {self.altura}. Su area es {self.calcular_area()}"
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def __str__(self):
        return f"El rectángulo es de base {self.base} y altura {self.altura}. Su area es {self.calcular_area()}"
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return self.radio * self.radio * 3.14
    def __str__(self):
        return f"El círculo es de radio {self.radio}. Su area es {self.calcular_area()}"
    

triangulo = Triangulo(3, 4)
print(triangulo.calcular_area())
print(triangulo)

rectangulo = Rectangulo(3, 4)
print(rectangulo.calcular_area())
print(rectangulo)

circulo = Circulo(3)
print(circulo.calcular_area())
print(circulo)
