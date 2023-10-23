class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def valor_total(self):
        valor_total = self.precio * self.cantidad
        print(f"Valor total de {self.nombre}: ${valor_total:.2f}")
        
    def __eq__(self, otro):
        if self.valor_total() == otro.valor_total():
            return True
        else:
            return False
producto1 = Producto("Arvejas", 30, 2)
producto2 = Producto("Cereales", 55, 5)

print(producto1 == producto2)