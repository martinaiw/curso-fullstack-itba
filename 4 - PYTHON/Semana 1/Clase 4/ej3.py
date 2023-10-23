persona = {
    "nombre":"",
    "edad": 0,
    "ciudad":"",
}
persona["nombre"] = input("Ingrese el nombre de la persona: ") 
persona["edad"] = input("Ingrese la edad de la persona: ") 
persona["ciudad"] = input("Ingrese la ciudad de la persona: ") 

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

valores = persona.values()
print(valores)