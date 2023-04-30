from math import pi
import sys
import errno


class ColorMessages:
    ERRO = '\033[91m'
    PADRAO = '\033[0m'


def calc_area(radius):
    return pi * float(radius) ** 2


def help():
    print(ColorMessages.ERRO,
          "[error] - É necessário informar o raio do círculo.")
    print("Sintaxe: {}(<radius>)".format(
        sys.argv[0]), ColorMessages.PADRAO)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print('O Raio deve ser um valor numérico')
        sys.exit(errno.EINVAL)
    else:
        radius = sys.argv[1]
        area = calc_area(radius)
        print('A área do círculo: ', area)
