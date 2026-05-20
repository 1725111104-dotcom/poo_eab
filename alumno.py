class Alumno:
    def __init__(self, nombre, edad, matricula, carrera, semestre,
                 promedio, correo, telefono, sexo, grupo):

        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.correo = correo
        self.telefono = telefono
        self.sexo = sexo
        self.grupo = grupo

        print(f"Nombre del alumno: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio}")
        print(f"Correo electrónico: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print(f"¿Hombre o mujer?: {self.sexo}")
        print(f"Grupo: {self.grupo}")

    def estudiar(self):
        print("El alumno está estudiando")

    def asistir_clase(self):
        print("El alumno está asistiendo a clase")

    def hacer_tarea(self):
        print("El alumno está haciendo la tarea")

    def presentar_examen(self):
        print("El alumno está presentando un examen")

    def descansar(self):
        print("El alumno está descansando")


Lalo = Alumno( "Eduardo Aguirre Barragán", 21, "1725111104", "TIC´s", 3,
              9.4, "lalo@gmail.com", "7761234567", "H", "31")

Lalo.estudiar()
Lalo.asistir_clase()
Lalo.hacer_tarea()
Lalo.presentar_examen()
Lalo.descansar()