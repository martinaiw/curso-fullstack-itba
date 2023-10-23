exito = 0
fallo = 0
with open('archivo.txt', 'r') as archivo:     
    for linea in archivo:
        print(linea)
        entrada = linea.split()
        exito += entrada.count("200")
        fallo += entrada.count("400") + entrada.count("404")
        
print("Cantidad de solicitudes exitosas:", exito)
print("Cantidad de solicitudes fallidas:", fallo)