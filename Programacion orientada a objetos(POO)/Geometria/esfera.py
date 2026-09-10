from figura import Figura

class Esfera(Figura):
    def __init__(self, radio):
        super().__init__("Esfera")
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * 3.1416 * (self.radio * self.radio * self.radio)