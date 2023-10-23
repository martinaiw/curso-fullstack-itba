while True:
    name = input("Ingrese su nombre: ")
    if not name:
        print("Error: El nombre no debe estar vacío.")
        continue
    age_str = input("Ingrese su edad: ")
    try:
        age = int(age_str)
        if age < 0:
            print("Error: La edad debe ser un número entero positivo.")
        else:
            print(f"¡Hola {name}! Tu edad es {age}.")
            break
    except ValueError:
        print("Error: La edad debe ser un número entero positivo.")
