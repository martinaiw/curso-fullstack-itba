files = []
n = int(input("Ingrese la cantidad de archivos que desea combinar(1 a 5):"))
final_file = open("final_file.txt", "a")
for i in range(1, n+1):
    with open(f"file{i}.txt", "r") as archivo:
        for linea in archivo:
            contenido = linea + "\n"
            final_file.write(contenido)
final_file.close()

print("Archivos combinados!")

