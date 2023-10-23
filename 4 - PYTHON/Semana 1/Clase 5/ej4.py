import gzip
import os
                        
nombre_original = input("Ingrese el nombre del archivo que desea comprimir: ")
nombre_comprimido = input("Ingrese el nombre del archivo comprimido: ")


with open(f'{nombre_original}.txt', 'rb') as archivo:
   with gzip.open(f'{nombre_comprimido}.gz', 'xb') as archivo_comprimido:
    contenido = archivo.read()
    archivo_comprimido.write(contenido)

print(f'Archivo {nombre_original}.txt comprimido como {nombre_comprimido}.gz')
tamano_original = os.path.getsize(f"{nombre_original}.txt")
tamano_comprimido = os.path.getsize(f"{nombre_comprimido}.gz")
print(f"El archivo original pesa {tamano_original} bytes y el comprimido {tamano_comprimido} bytes")