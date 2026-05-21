class Smartphone:
    def __init__ (self, tamano, peso, forma, procesador, memoria_ram,
                  resolucion_camaras, capacidad_bateria, almacenamiento,
                  tamano_pantalla, numero_botones):
        self.tamano = tamano
        self.peso = peso
        self.forma = forma
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.resolucion_camaras = resolucion_camaras
        self.capacidad_bateria = capacidad_bateria
        self.almacenamiento = almacenamiento
        self.tamano_pantalla = tamano_pantalla
        self.numero_botones = numero_botones
        print(f"Tamaño del teléfono: {self.tamano}")
        print(f"Peso del smartphone:{self.peso}")
        print(f"Forma del smartphone:{self.forma}")
        print(f"Nombre del procesador:{self.procesador}")
        print(f"Capacidad de la memoria RAM:{self.memoria_ram}")
        print(f"Resolución de la cámara principal:{self.resolucion_camaras}")
        print(f"Capacidad de la batería:{self.capacidad_bateria}")
        print(f"Capacidad de almacenamiento:{self.almacenamiento}")
        print(f"Tamaño de la pantalla:{self.tamano_pantalla}")
        print(f"Número de botones:{self.numero_botones}")

    def llamar (self):
        print("Esta llamando")
    def mensajear (self):
        print("Esta mensajeando")
    def juegar (self):
        print("Esta jugando")
    def fotografiar (self):
        print("Esta tomando fotos")
    def videar (self):
        print("Esta videando")
        
s30 = Smartphone(9.1, 150, "Rectangular", "Snapdragon 8 gen", 16, 200,
                 4000, 1000, 8.8, 3)
s30.llamar()
s30.mensajear()
s30.juegar()
s30.fotografiar()
s30.videar()
