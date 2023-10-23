# En  el  archivo  descriptives.py,  define  al  menos  dos  funciones  o  clases  que 
# realicen  cálculos  descriptivos  sobre  conjuntos  de  datos,  como  calcular  la 
# media, la mediana, la desviación estándar, etc.

def media (conjunto):
    media = 0
    for i in range(0, len(conjunto)):
        media+=conjunto[i]
    return media/len(conjunto)    

def mediana (conjunto):
    conjunto_ordenado = list(conjunto)
    conjunto_ordenado.sort()
    if len(conjunto_ordenado)%2 != 0:
        return conjunto_ordenado[len(conjunto_ordenado)//2]
    else:
        return ((conjunto_ordenado[(len(conjunto_ordenado)//2)-1]+conjunto_ordenado[len(conjunto_ordenado)//2])/2)

def moda (conjunto):
    conjunto_list = list(conjunto)
    conjunto_list.sort()
    aux_list = []
    max_repeats = 1
    #tengo que recorred todo el arreglo y ver cual es el elemento que más se repite 
    for i in range(1, len(conjunto_list)):
        if conjunto_list.count(i) > max_repeats:
            max_repeats = conjunto_list.count(i)
            moda = conjunto_list[i]
    return moda
