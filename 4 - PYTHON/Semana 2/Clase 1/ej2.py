def dividir_seguro(a, b):
    while True:
        try:
            num1 = int(a)
            num2 = int(b)
            resultado = num1/num2
        except ValueError:
            print("Error: uno o ambos valores no son números.")
            break
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
            break
        else:
            print(f"El resultado es: {resultado}")
            break
        
        
a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")
dividir_seguro(a, b)