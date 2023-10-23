errores = [0, 0, 0, 0]
with open("archivo5.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
        entrada = linea.split()
        errores[0] += entrada.count("ErrorType1")
        errores[1] += entrada.count("ErrorType2")
        errores[2] += entrada.count("ErrorType3")
        errores[3] += entrada.count("ErrorType4")

print(
    f"Cantidad de ocurrencia por error: \nErrortype1: {errores[0]} \nErrortype2: {errores[1]} \nErrortype3: {errores[2]} \nErrortype4: {errores[3]}"
)
