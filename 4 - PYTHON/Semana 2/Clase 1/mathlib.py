def raiz_cuadrada(num):
    assert num >=0
    return num**0.5
    
def suma_tuplas(tupla1, tupla2):
    assert len(tupla1) == len(tupla2)
    tupla_resultado = []
    for i in range(0, len(tupla1)):
        suma = tupla1[i] + tupla2[i]
        tupla_resultado.append(suma)
    return tuple(tupla_resultado)

def calcular_area_circulo(radio):
    assert(radio > 0)
    area = 3.14*(radio**2)
    return area