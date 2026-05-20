class SillaReclinable:
    def __init__(self, material, color, tipo_tela, altura, ancho,
                 peso, reclinable, reposabrazos, marca, precio):

        self.material = material
        self.color = color
        self.tipo_tela = tipo_tela
        self.altura = altura
        self.ancho = ancho
        self.peso = peso
        self.reclinable = reclinable
        self.reposabrazos = reposabrazos
        self.marca = marca
        self.precio = precio

        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Tipo de tela: {self.tipo_tela}")
        print(f"Altura: {self.altura}")
        print(f"Ancho: {self.ancho}")
        print(f"Peso máximo soportado: {self.peso}")
        print(f"¿Es reclinable?: {self.reclinable}")
        print(f"¿Tiene reposabrazos?: {self.reposabrazos}")
        print(f"Marca: {self.marca}")
        print(f"Precio: {self.precio}")

    def reclinar(self):
        print("La silla se reclina")

    def sentarse(self):
        print("Una persona se sienta en la silla")

    def ajustar_respaldo(self):
        print("El respaldo se ajusta")

    def descansar(self):
        print("La silla ayuda a descansar")

    def mover(self):
        print("La silla se mueve")


silla1 = SillaReclinable("Cuero", "Negro", "Piel sintética", "120 cm", "80 cm",
                         "150 kg", "Sí", "Sí", "ComfortPlus", "$7,500")

silla1.reclinar()
silla1.sentarse()
silla1.ajustar_respaldo()
silla1.descansar()
silla1.mover()