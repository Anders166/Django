from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_volumen(self):
        pass

    def mostrar_info(self):
        volumen = self.calcular_volumen()
        print(f"Figura: {self.nombre}")
        print(f"Volumen: {volumen:.2f}")
        print("")