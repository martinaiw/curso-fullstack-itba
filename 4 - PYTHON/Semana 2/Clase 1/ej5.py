import stats.descriptives as desc
import stats.visualizations as vis

datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

vis.generar_histograma(datos, "Histograma de Datos", "Valores", "Frecuencia")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

vis.generar_grafico_dispersion(x, y, "Gráfico de Dispersión", "Eje X", "Eje Y")


conjunto = (2,6,1,8,5,2,3,3,3,3,3)
res = desc.mediana(conjunto)
res2 = desc.moda(conjunto)
conjunto_sorted = list(conjunto)
conjunto_sorted.sort()
print(f"Mediana del conjunto {conjunto_sorted} es {res}")
print(f"Moda del conjunto {conjunto_sorted} es {res2}")