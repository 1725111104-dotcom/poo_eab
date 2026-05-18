class PersonajeRpg:
    def __init__(self, genero, raza, equipamiento, altura, fuerza,
                 velocidad, idioma, inteligencia, edad, nombre_apodo):
        self.genero = genero
        self.raza = raza
        self.equipamiento = equipamiento
        self.altura = altura
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.idioma = idioma
        self.inteligencia = inteligencia
        self.edad = edad
        self.nombre_apodo = nombre_apodo
        print(f"Género:{self.genero}")
        print(f"Raza:{self.raza}")
        print(f"Equipamiento:{self.equipamiento}")
        print(f"Altura:{self.altura}")
        print(f"Fuerza:{self.fuerza}")
        print(f"Velocidad:{self.velocidad}")
        print(f"Idioma:{self.idioma}")
        print(f"Inteligencia:{self.inteligencia}")
        print(f"Edad:{self.edad}")
        print(f"Nombre o apodo:{self.nombre_apodo}")
    def correr (self):
        print(f"Está corriendo")
    def saltar (self):
        print(f"Está saltando")
    def golpear (self):
        print(f"Está golpeando")
    def comer (self):
        print(f"Está comiendo")
    def agacharse (self):
        print(f"Está agachándose")

Lalo = PersonajeRpg("Hombre", "Asiática", "2 pistolas", "32 pixeles", 
                    "99/999", "6 casillas por turno", "Español", "Alta",
                    20, "Lalo")
Lalo.correr()
Lalo.saltar()
Lalo.golpear()
Lalo.comer()
Lalo.agacharse()


