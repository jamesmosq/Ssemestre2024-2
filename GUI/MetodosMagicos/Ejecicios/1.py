"""

1.	__init__: En el ejemplo del Libro, usamos __init__ para inicializar un libro con su título,
autor y número de páginas.
Este método se llama automáticamente cuando creamos una nueva instancia de Libro.
"""
# 1. __init__
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

libro = Libro("El Quijote", "Miguel de Cervantes", 863)
print(f"Libro creado: {libro.titulo} por {libro.autor}")