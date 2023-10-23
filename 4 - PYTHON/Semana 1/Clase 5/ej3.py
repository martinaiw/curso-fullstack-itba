import csv

ventas_por_producto = {}
with open("productos.csv", "r") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # saltea el encabezado
    for fila in lector_csv:
        producto = fila[0]
        cantidad_vendida = int(fila[1])
        precio_unitario = float(fila[2])
        total_ventas_producto = cantidad_vendida * precio_unitario

        if producto in ventas_por_producto:
            ventas_por_producto[producto] += total_ventas_producto
        else:
            ventas_por_producto[producto] = total_ventas_producto
            
ventas_ordenadas = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)

for producto, total_ventas in ventas_ordenadas:
    print(f"{producto}: ${total_ventas}")

#####profe en clases
import csv
from collections import defaultdict
ventas=defaultdict(float)

with open('ventas.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        ventas[row['Producto']]+=float(row['Cantidad'])*float(row['Precio unitario'])

for producto, total in sorted(ventas.items(),key=lambda x:x[1],reverse=True):
    print(f"{producto}: ${total:.2f}")

# import csv

# with open('ejemplo.csv','w',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['Nombre','Edad'])
#     writer.writerow(['Juan','19'])
#     writer.writerow(['Ana','22'])
#     writer.writerow(['Cami','25'])
