list1 = [1, 2, 3, 12, 2, 4, 1, 2, 1, 2, 5, 1, 2, 8, 31, 231, 23, 123, 1, 23]
list2 = [4, 5, 6, 3, 354, 34, 7, 1, 1, 21, 2, 8, 1, 0, 123, 123, 2, 1]

conj1 = set(list1)
conj2 = set(list2)

numeros_comunes = conj1.intersection(conj2)
print(numeros_comunes)
