try: 
    archivo = open('archivo.txt', 'r')
except FileNotFoundError: 
    print("Error: Archivo no encontrado.") 
except IOError as e:
    print(f"Error al leer el archivo: {e}")
else:
    for linea in archivo:
        print(linea) 
    archivo.close()