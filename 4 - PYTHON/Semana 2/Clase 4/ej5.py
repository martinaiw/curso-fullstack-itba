class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def valor_total(self):
        return self.precio * self.cantidad

    def __eq__(self, otro):
        if self.nombre == otro.nombre:
            return True
        else:
            return False


class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

class Carrito:
    def __init__(self, tienda):
        self.valor_total = 0
        self.productos = []
        self.tienda = tienda

    def agregar_al_carrito(self, otro_producto, cantidad):
        for producto in self.tienda.inventario:
            if producto.nombre == otro_producto.nombre:
                if producto.cantidad >= cantidad:
                    self.productos.append(Producto(producto.nombre, cantidad, producto.precio))
                    producto.cantidad -= cantidad
                else:
                    print(f"No hay suficientes unidades de {otro_producto.nombre} en el inventario.")
                break

    def eliminar_del_carrito(self, producto, cantidad):
        for item in self.tienda.inventario:
            if producto.nombre == item.nombre:
                item.cantidad += cantidad
        self.productos.remove(producto)

    def calcular_total_compra(self):
        total = sum(producto.valor_total() for producto in self.productos)
        return total

tienda = Tienda()
tienda.agregar_producto(Producto("Arvejas", 50, 23))
tienda.agregar_producto(Producto("Tomates", 50, 56))
tienda.agregar_producto(Producto("Milanesas", 50, 300))
tienda.agregar_producto(Producto("Ravioles", 50, 400))
tienda.agregar_producto(Producto("Papas fritas", 50, 21))
tienda.agregar_producto(Producto("Brocoli", 50, 30))

carrito = Carrito(tienda)
carrito.agregar_al_carrito(tienda.inventario[0], 3)
carrito.agregar_al_carrito(tienda.inventario[5], 20)

print("Inventario de la tienda:")
for producto in tienda.inventario:
    print(f"{producto.nombre}: {producto.cantidad} uds. --- ${producto.precio:.2f}")

print("\nCarrito de compras:")
for producto in carrito.productos:
    print(f"{producto.nombre}: {producto.cantidad} unidades --- ${producto.precio * producto.cantidad :.2f}")

total_compra = carrito.calcular_total_compra()
print(f"\nTotal de la compra en el carrito: ${total_compra:.2f}")
