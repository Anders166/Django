#:Dqdjdhasjkhjhaajdhjufuiui
class Cuenta:
    def __init__(self, numero, saldo):#Constructor
        self.__saldo = saldo #Protegido
        self.numero = numero #Publico
    
    def depositar(self, cantidad): #Metodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad #Acumulador
            
    #Agregar el metodo retirar
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")
            
    def ImprimirSaldo(self):
        print(f"El saldo de la cuenta {self.numero} es: {self.__saldo}")
    
#Creacion del objeto
cuenta1= Cuenta(1111,1000)
cuenta1.depositar(999)
print(cuenta1.ImprimirSaldo())

#Crear un repositorio en git que contendra todo lo que hara en Django
#Subir este ejercicio a git
#Enviar el enlace a dilopezz@sena.edu.co


