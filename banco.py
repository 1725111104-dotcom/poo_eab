class Banco:
    def __init__ (self, no_clientes, no_elementos_seguridad, no_edificios,
                  sistema_informatico, nombre_banco, no_cajeros, fiable,
                  capital, horario_atencion, color_banco):
        self.no_clientes = no_clientes
        self.no_elementos_seguridad = no_elementos_seguridad
        self.no_edificios = no_edificios
        self.sistema_informatico = sistema_informatico
        self.nombre_banco = nombre_banco
        self.no_cajeros = no_cajeros
        self.fiable = fiable
        self.capital = capital
        self.horario_atencion = horario_atencion
        self.color_banco = color_banco
        print(f"Número de clientes:{self.no_clientes}")
        print(f"Número de elementos de seguridad:{self.no_elementos_seguridad}")
        print(f"Número de edificios:{self.no_edificios}")
        print(f"Sistema informático:{self.sistema_informatico}")
        print(f"Nombre del banco:{self.nombre_banco}")
        print(f"Número de cajeros:{self.no_cajeros}")
        print(f"¿Es fiable?:{self.fiable}")
        print(f"Capital:{self.capital}")
        print(f"Horario de atención a clientes:{self.horario_atencion}")
        print(f"Color del banco:{self.color_banco}")
    def retirar (self):
        print("Esta retirando dinero")
    def pagar (self):
        print("Esta haciendo el pago")
    def prestamo (self):
        print("Se realizó un prestamo")
    def transferencia (self):
        print("Se hizo la transferencia con éxito")
    def depositar (self):
        print("Se realizó el depósito con éxito")
acme = Banco (10000, None, None, "ACME 0.1", "ACME", 10000,
              True, 1000000, "9:00 a 19:00", "Verde fosfo")
acme.retirar()
acme.pagar()
acme.prestamo()
acme.transferencia()
acme.depositar()