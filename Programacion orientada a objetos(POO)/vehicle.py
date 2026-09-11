class Vehicle:
    def __init__(self,brand,color,plate):#init con 2 guiones bajos __ __
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
        
    def acelerar (self):
        self.speed += 10
        print(f"El {self.brand} acelero a {self.speed} km/h")

    def desacelerar (self):
        self.speed -= 5
        print(f"El {self.brand} desacelero a {self.speed} km/h")

#Creacion de los objetos
my_vehicle = Vehicle('Hunday','Black','ABD-124')
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()

#Agregar el atributo plate y el metodo desacelerar;
#Crear el objeto
#Acelerar 2 veces
#Desacelerar 3 veces
#subir a git dentro del repositorio de ayer
