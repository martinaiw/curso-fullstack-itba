import ejercicios.libros as libros

libro1 = libros.Libro("Harry Potter", "J. K. Rowling", 567)
libro2 = libros.Libro("OSTEP", "Arpacci-Dusseau", 421)
libro3 = libros.Libro("El Gato Negro", "Edgar Allan Poe", 100)

print(libro1)
print(libro2)
print(libro3)

print(libro1 == libro2)
print(libro1 == libro3)
print(libro2 == libro3)


