from figura import Figura

class Cubo(Figura):
    def __init__(self, lado):
        super().__init__("Cubo")
        self.lado = lado

    def calcular_volumen(self):
        return (self.lado * self.lado * self.lado)