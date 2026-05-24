class Perro:
    def __init__(self, nombre, raza, color, edad, peso, tamano,
                 tipo_alimento, energia, dueno, precio):

        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad
        self.peso = peso
        self.tamano = tamano
        self.tipo_alimento = tipo_alimento
        self.energia = energia
        self.dueno = dueno
        self.precio = precio

        print(f"Nombre del perro: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Tamaño: {self.tamano}")
        print(f"Tipo de alimento: {self.tipo_alimento}")
        print(f"Nivel de energía: {self.energia}")
        print(f"Dueño: {self.dueno}")
        print(f"Precio: {self.precio}")

    def ladrar(self):
        print("El perro ladra")

    def correr(self):
        print("El perro corre")

    def comer(self):
        print("El perro está comiendo")

    def dormir(self):
        print("El perro está durmiendo")

    def mover_la_cola(self):
        print("El perro mueve la cola")


perro1 = Perro("Max", "Labrador", "Café", "3 años", "30 kg",
    "Grande", "Croquetas", "Alta", "Eduardo", "$8,000")

perro1.ladrar()
perro1.correr()
perro1.comer()
perro1.dormir()
perro1.mover_la_cola()