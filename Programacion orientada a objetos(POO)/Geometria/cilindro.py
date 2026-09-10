from figura import Figura

class Cilindro(Figura):
    def __init__(self, radio, altura):
        super().__init__("Cilindro")
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return 3.1416 * (self.radio*self.radio) * self.altura