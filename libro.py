class Libro:
    def __init__ (self, color, no_paginas, autor, anio, editorial, material_pasta,
                  titulo, codigo, categoria, ilustrado):
        
        self.color = color
        self.no_paginas = no_paginas
        self.autor = autor
        self.anio = anio
        self.editorial = editorial
        self.material_portada = material_pasta
        self.titulo = titulo
        self.codigo = codigo
        self.categoria = categoria
        self.ilustrado = ilustrado

        print(f"El color del libro es: {self.color}")
        print(f"Número de páginas: {self.no_paginas}")
        print(f"Nombre del autor: {self.autor}")
        print(f"Año de publicación: {self.anio}")
        print(f"Nombre de la editorial: {self.editorial}")
        print(f"Material de la pasta: {self.material_portada}")
        print(f"Título del libro: {self.titulo}")
        print(f"Código de identificación: {self.codigo}")
        print(f"Categoría: {self.categoria}")
        print(f"¿Está ilustrado?: {self.ilustrado}")

    def leer (self):
        print("Leer el libro")

    def guardar (self):
        print("Guardar el libro")

    def acomodar (self):
        print("Acomodar el libro")

    def hojear (self):
        print("Hojear el libro")

    def prestar (self):
        print("Prestar el libro")

Como_entrenar_a_tu_dragon = Libro ("Rojo", 255, "María Pérez Sánchez",
                                   2008, "Trillas", "Blanda", "Cómo entrenar a tu dragón", "1112-21234-232347684319",
                                   "Aventura", True)

Como_entrenar_a_tu_dragon.leer()
Como_entrenar_a_tu_dragon.guardar()
Como_entrenar_a_tu_dragon.acomodar()
Como_entrenar_a_tu_dragon.hojear()
Como_entrenar_a_tu_dragon.prestar()
