while True:
    try:
        n = int(input("Ingrese un número mayor que 1: "))
        if n <= 1:
            print("Ingresaste un número menor o igual a 1!")
            break
        else:
            l = list([0, 1])  # casos base
            for i in range(0, n + 1):
                fib = l[i] + l[i + 1]
                l.append(fib)
                print(f"Fib({i}):", l[i])

    except ValueError:
        print("Entrada inválida")

###ejercicio invertir while martes
# i = 10
# while i > 1:
#     print(2 * i, "\t")

#     i = i - 1
