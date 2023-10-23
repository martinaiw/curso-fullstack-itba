while True:
    try:
        n = int(input("Ingrese un numero mayor que 1: "))
        suma_pares = 0
        suma_impares = 0
        if 1 <= n:
            break
        else:
            print(">>Número fuera del rango")
    except ValueError:
        print(">>Entrada inválida")

for i in range(n + 1): # n inclusive, si no, range(n) si n exclusive
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print("Suma pares:", suma_pares)
print("Suma impares:", suma_impares)
