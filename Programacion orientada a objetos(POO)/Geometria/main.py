from cubo import Cubo
from esfera import Esfera
from cilindro import Cilindro
from figura import Figura


def main():
    cubo = Cubo(lado=4)
    esfera = Esfera(radio=3)
    cilindro = Cilindro(radio=2, altura=5)
    figuras: list[Figura] = [cubo, esfera, cilindro]
    for figura in figuras:
        figura.mostrar_info()

if __name__ == "__main__":
    main()