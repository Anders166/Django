#1-Definicion de la clase (El plano)
class Auto:
    def _init_ (self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0

    def acelerar (self):
        self.velocidad += 10
        print(f"El {self.marca} acelero a {self.velocidad} km/h")

#2 Creacion de objetos (Instancion)
mi_auto = Auto("Toyota","Rojo")
mi_auto.acelerar() #Impresion: EL toyota acelero a 10km/h