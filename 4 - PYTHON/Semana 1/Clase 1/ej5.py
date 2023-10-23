#s = input("Ingrese su nombre completo: ")
# s_apellido = s.index(" ")

# if (s[0] == s[0].lower()) & (s[s_apellido + 1] == s[s_apellido + 1].upper()):
#     s = s.replace(s[0], s[0].upper())
#     s = s.replace(s[1:s_apellido], s[1:s_apellido].lower())
#     s = s.replace(s[s_apellido + 2 :], s[s_apellido + 2 :].lower())

# elif (s[0] == s[0].upper()) & (s[s_apellido + 1] == s[s_apellido + 1].lower()):
#     s = s.replace(s[s_apellido + 1], s[s_apellido + 1].upper())
#     s = s.replace(s[1:s_apellido], s[1:s_apellido].lower())
#     s = s.replace(s[s_apellido + 2 :], s[s_apellido + 2 :].lower())

# elif (s[0] == s[0].lower()) & (s[s_apellido + 1] == s[s_apellido + 1].lower()):
#     s = s.replace(s[0], s[0].upper())
#     s = s.replace(s[s_apellido + 1], s[s_apellido + 1].upper())
#     s = s.replace(s[1:s_apellido], s[1:s_apellido].lower())
#     s = s.replace(s[s_apellido + 2 :], s[s_apellido + 2 :].lower())

# elif (s[0] == s[0].upper()) & (s[s_apellido + 1] == s[s_apellido + 1].upper()):
#     s = s.replace(s[1:s_apellido], s[1:s_apellido].lower())
#     s = s.replace(s[s_apellido + 2 :], s[s_apellido + 2 :].lower())
# print(s)

#version más eficiente con funciones:

s = input("Ingrese su nombre completo: ")

# Divide el nombre en palabras
nombres = s.split()

# Convierte el primer nombre a mayúsculas
primer_nombre = nombres[0].capitalize()

# Convierte el primer carácter de cada apellido a mayúsculas
apellidos = [apellido.capitalize() for apellido in nombres[1:]]

# Combina el primer nombre con los apellidos en una sola cadena
nombre_completo = primer_nombre + " " + " ".join(apellidos)

print(nombre_completo)
