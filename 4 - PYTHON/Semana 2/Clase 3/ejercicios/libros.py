import datetime as date 

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    fecha_publicacion = date.date.today()
        
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_paginas(self):
        return self.paginas
    def __str__(self):
        return f"El libro se llama {self.titulo}, fue escrito por {self.autor}, publicado el {self.fecha_publicacion} y cuenta con {self.paginas} páginas."
    def set_titulo(self, titulo):
        try: 
            if titulo is None:
                raise ValueError
        except ValueError:
            print("El titulo del libro no puede estar vacío!")
            
    def __eq__(self,other):
        return self.titulo == other.titulo and self.autor == other.autor and self.paginas == other.paginas and self.fecha_publicacion == other.fecha_publicacion
    
    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    
