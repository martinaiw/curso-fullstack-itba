def contar_vocales(s):
    conteo = list([0,0,0,0,0])
    s = s.lower()
    for i in s:
        if i == 'a':
            conteo[0]+=1
        elif i == 'e':
            conteo[1]+=1
        elif i == 'i':
            conteo[2]+=1
        elif i == 'o':
            conteo[3]+=1
        elif i == 'u':
            conteo[4]+=1
    return conteo

s = input("Ingrese una palabra: ")

print(f"Tu palabra tiene: {contar_vocales(s)} vocales")

def contar_vocales2(str):

    vocales = ["a", "e", "i", "o", "u"]

    contador = [0, 0, 0, 0, 0]

    for x in str:

        if x in vocales:

            contador[vocales.index(x)] = contador[vocales.index(x)]+1

    return contador

def contar_vocales3(texto):

    return [(1 if letra in "aeiou" else 0) for letra in texto.lower()]

