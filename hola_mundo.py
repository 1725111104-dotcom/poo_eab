class HolaMundo:
    def __init__(self):
        print(f"Constructor")

    def metodoUno(self):
        print("Método uno")

    def metodoDos(self, numero_uno:int, numero_dos:int)->int:
    """
    Este método realiza la suma de dos números enteros y regresa
    el resultado

    Args:
        numero_uno:int - Primer número para la suma
        numero_dos:int - Segundo número para la suma
    
    Returns:
        resultado:int - Variable con el resultado de la suma
    """

        resultado = numero_uno + numero_dos
        return resultado
    
    def metodoTres(self, numero_uno, numero_dos, rfc):
        resultado = numero_uno + numero_dos
        return resultado

    def metodoCuatro(self, numero_uno, numero_dos)-> None:
        resultado = numero_uno + numero_dos
        print(f"La suma es {resultado}")


nombre_objeto = HolaMundo()