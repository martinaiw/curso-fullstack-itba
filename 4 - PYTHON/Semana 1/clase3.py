def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)


def calificacion_mas_alta(lista_promedios):
    return max(lista_promedios)


def calificacion_mas_baja(lista_promedios):
    return min(lista_promedios)


def estudiantes_sobresalientes(estudiantes, promedio_clase):
    for estudiante in estudiantes:
        if estudiante["promedio_calificaciones"] > promedio_clase:
            print(f"  -Nombre: {estudiante['nombre']}")
            print(f"  -Apellido: {estudiante['apellido']}")
            print(
                f"  -Promedio de Calificaciones: {estudiante['promedio_calificaciones']}"
            )
            print()


def chequear_input():
    n = input(f"Ingrese la nota: ")

    while True:
        try:
            if 1 <= float(n) <= 100:
                break
            else:
                n = float(input("Ingrese una nota valida: "))
        except ValueError:
            n = float(input("Ingresaste una letra! Por favor ingresa un numero: "))

    return float(n)

estudiantes = list()
num_estudiantes = int(input("Ingrese el numero de estudiantes: "))
lista_promedios = list()


for i in range(num_estudiantes):
    estudiante = dict()
    estudiante["nombre"] = input("Ingrese el nombre: ")
    estudiante["apellido"] = input("Ingrese el apellido: ")
    estudiante["nota_1"] = chequear_input()
    estudiante["nota_2"] = chequear_input()
    estudiante["nota_3"] = chequear_input()
    estudiante["promedio_calificaciones"] = calcular_promedio(
        [estudiante["nota_1"], estudiante["nota_2"], estudiante["nota_3"]]
    )
    estudiantes.append(estudiante)
    lista_promedios.append(estudiante["promedio_calificaciones"])
    print("Estudiante añadido!\n")

for i, estudiante in enumerate(estudiantes):
    print(f">>Estudiante {i + 1}:")
    print("  -Nombre:", estudiante["nombre"])
    print("  -Apellido:", estudiante["apellido"])
    print("  -Promedio de calificaciones:", estudiante["promedio_calificaciones"])
    print()

print(">>Lista de promedios de la clase", lista_promedios)
print()
print(">>Calificacion mas alta de la clase:", calificacion_mas_alta(lista_promedios))
print()
print(">>Calificacion mas baja de la clase:", calificacion_mas_baja(lista_promedios))
promedios_clase = calcular_promedio(lista_promedios)
print()
print(">>Promedio de calificaciones de la clase: ", promedios_clase)
print()
print(">>Estudiantes con promedio superior al promedio de la clase:")
estudiantes_sobresalientes(estudiantes, promedios_clase)
