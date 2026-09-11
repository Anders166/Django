#Clase Padre: La clase padre no sabe exactamente como calcular un salario, las clases hijas si
from abc import ABC, abstractmethod #Abstract Base Class

class Empleado(ABC):
    def __init__(self,nombre,documento,salario):#Construccion de la clase o molde, parameteros
        self.nombre = nombre#Atributo
        self.documento= documento#Atributo
        self.__salario = salario#Atributo

    @abstractmethod#Metodo abstracto
    def calcular_bonificacion(self):
        pass #No hace nada

    @property #Accediendo a un atributo privado
    def salario(self):
        return self.__salario

    def mostrar_informacion(self):#Metodo
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Salario: {self.salario:,.0.f}")#0.f decimales

    def __str__(self):#Metodo, prueba unitaria
        return f"Nombre: {self.nombre} - Documento: {self.documento}"
              