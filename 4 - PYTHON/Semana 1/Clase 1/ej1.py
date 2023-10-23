# estoy agregando un comentario
# print(2 + 3)
# print("I love Baisin")
# para ejecutar eso ponemos ./clase.py o ./clase

############################################################
# Ejercicio 1


while True:
    try:
        n = int(input("Ingrese un número entero entre 1 y 100: "))
        if 1 <= n & n <= 100:
            break
        else:
            print("Número fuera del rango")
    except ValueError:
        print("Entrada inválida")
        
if (n % 2) != 0:
    print("Weird")
elif (n % 2) == 0 & 2 <= n & n <= 5:
    print("Not Weird")
elif (n % 2) == 0 & 6 <= n & n <= 20:
    print("Not Weird")
elif (n % 2) == 0 & n > 20:
    print("Weird")
