class Mesa:
    def __init__(self, material, color, forma, altura, ancho,
                 largo, numero_patas, peso, uso, precio):

        self.material = material
        self.color = color
        self.forma = forma
        self.altura = altura
        self.ancho = ancho
        self.largo = largo
        self.numero_patas = numero_patas
        self.peso = peso
        self.uso = uso
        self.precio = precio

        print(f"Material de la mesa: {self.material}")
        print(f"Color: {self.color}")
        print(f"Forma: {self.forma}")
        print(f"Altura: {self.altura}")
        print(f"Ancho: {self.ancho}")
        print(f"Largo: {self.largo}")
        print(f"Número de patas: {self.numero_patas}")
        print(f"Peso: {self.peso}")
        print(f"Uso: {self.uso}")
        print(f"Precio: {self.precio}")

    def sostener_objetos(self):
        print("La mesa sostiene objetos")

    def mover(self):
        print("La mesa se mueve")

    def limpiar(self):
        print("La mesa está siendo limpiada")

    def decorar(self):
        print("La mesa está decorando el espacio")

    def doblar(self):
        print("La mesa se puede doblar")


mesa1 = Mesa(
    "Madera", "Café", "Rectangular", "75 cm", "90 cm",
    "180 cm", 4, "25 kg", "Comedor", "$4,500"
)

mesa1.sostener_objetos()
mesa1.mover()
mesa1.limpiar()
mesa1.decorar()
mesa1.doblar()