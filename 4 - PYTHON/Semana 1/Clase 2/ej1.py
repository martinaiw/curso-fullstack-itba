def calcular_promedio(num):
    sum = 0
    for i in num:
        sum+=i
    prom = sum/len(num)
    return prom
def calcular_promedio2(num):
    return sum(num)/(len(num))

num = [1,6,2,7]
print(calcular_promedio(num))
num = [1,6,2,7]
print(calcular_promedio2(num))