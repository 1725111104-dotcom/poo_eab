class Coche:
  def __init__(self, marca, modelo, color, velocidad_max, tipo_combustible,
               numero_puertas, transmision, cilindros, capacidad_maletero,
               precio):
                 self.marca = marca
                 self.modelo = modelo
                 self.color = color
                 self. velocidad_max = velocidad_max
                 self.tipo_combustible = tipo_combustible
                 self.numero_puertas = numero_puertas
                 self.transmisio = transmision
                 self.cilindros = cilindros
                 self. capacidad_maletero = capacidad_maletero
                 self.precio = precio
                 print(f"Marca del coche:{self.marca}")
                 print(f"Nombre del modelo:{self.modelo}")
                 print(f"Color:{self.color}")
                 print(f"Velocidad máxima:{self.velocidad_max}")
                 print(f"Tipo de combustible:{self.tipo_combustible}")
                 print(f"Número de puertas:{self.numero_puertas}")
                 print(f"Transmisión{self.transmision}")
                 print(f"Cilindros:{self.cilindros}")
                 print(f"Capacidad de maletero:{self.capacidad_maletero}")
                 print(f"Precio:{self.precio}")
    def encender(self):
      print(f"El coche enciende")
    def acelerar(self):
      print(f"El coche acelera")
    def tocar_el_claxon(self):
      print(f"El cohce toca el claxon")
    def frenar(self):
      print(f"El coche frena")
    def reversa(self):
      print(f"El coche va de reversa")
coche1 = Coche("Toyota", "Corolla", "Rojo", "220 km/h", "Gasolina", 4, "Automática",
               4, "470 litros", "$350,000")
coche1.encender()
coche1.acelerar()
coche1.tocar_claxon()
coche1.frenar()
coche1.reversa()
                      
