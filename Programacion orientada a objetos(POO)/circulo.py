import math

class Figura:
    def __init__(self, largo):
        self.largo = largo

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        return self.largo ** 2

    def calcular_perimetro(self):
        return 4 * self.largo

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(radio)

    def area(self):
        return math.pi * (self.largo ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.largo

mi_cuadrado = Cuadrado(lado=5)
print(f"Cuadrado - Área: {mi_cuadrado.area()}")
print(f"Cuadrado - Perímetro: {mi_cuadrado.calcular_perimetro()}")

mi_circulo = Circulo(radio=3)
print(f"Círculo - Área: {mi_circulo.area():.2f}")
print(f"Círculo - Perímetro: {mi_circulo.calcular_perimetro():.2f}")


    
