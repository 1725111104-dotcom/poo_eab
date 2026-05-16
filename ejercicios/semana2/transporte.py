class Transporte:
    def __init__(self, marca, modelo, color, precio, peso,
                 numero_pasajeros, tipo_combustible,
                 numero_llantas, pais_origen, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.peso = peso
        self.numero_pasajeros = numero_pasajeros
        self.tipo_combustible = tipo_combustible
        self.numero_llantas = numero_llantas
        self.pais_origen = pais_origen
        self.velocidad_max = velocidad_max
        print(f"Marca del coche: {self.marca}")
        print(f"Nombre del modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Peso en kilogramos: {self.peso}")
        print(f"Número de pasajeros: {self.numero_pasajeros}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
        print(f"Número de llantas: {self.numero_llantas}")
        print(f"País de origen: {self.pais_origen}")
        print(f"Velocidad máxima: {self.velocidad_max}")
    def avanzar(self):
        print("El transporte avanza")
    def frenar(self):
        print("El transporte frena")
    def encender(self):
        print("El transporte enciende")
    def acelerar(self):
        print("El transporte acelera")
    def girar(self):
        print("El transporte gira")

transporte1 = Transporte("Mercedes", "Sprinter", "Negro", "$800,000", 
                         "3500 kg", 4, "Diésel", 4, "Alemania", "180 km/h")
transporte1.avanzar()
transporte1.frenar()
transporte1.encender()
transporte1.acelerar()
transporte1.girar()
  
