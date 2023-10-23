import mathlib 

numero = 9
tupla1 = (1,1,2)
tupla2 = (5,0,3)
radio = 6

area = mathlib.calcular_area_circulo(radio)
nueva_tupla = mathlib.suma_tuplas(tupla1, tupla2)
raiz = mathlib.raiz_cuadrada(numero)

print(f"El area del círculo de radio {radio} es {area}")
print(f"La suma de las tuplas {tupla1} y {tupla2} es {nueva_tupla}")
print(f"La raiz cuadrada de {numero} es {raiz}")
