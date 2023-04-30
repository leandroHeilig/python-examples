from math import pi


def calc_area(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    radius = input('Informe o raio:')
    area = calc_area(radius)
    print('A área do círculoa é: ', area)
