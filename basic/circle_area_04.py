from math import pi


def calc_area(radius):
    print('Área do Circulo:', pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Informe o raio:')
    calc_area(radius)
