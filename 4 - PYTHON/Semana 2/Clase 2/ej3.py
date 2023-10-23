class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
        
    def perimetro(self):
        return self.base*2 + self.altura*2
        
    def __eq__(self, otro):
        if self.base == otro.base and self.altura == otro.altura:
            return True
        else:
            return False

rect1 = Rectangulo(3, 5)
rect2 = Rectangulo(4, 7)
print(f"Rectangulo 1: Area {rect1.area()}, Perimetro {rect1.perimetro()}")
print(f"Rectangulo 2: Area {rect2.area()}, Perimetro {rect2.perimetro()}")
print(rect1 != rect2)
