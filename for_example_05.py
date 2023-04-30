from random import randint


def sortear():
    return randint(1, 6)


for i in range(1, 7):
    if (i % 2 == 1):
        continue

    if sortear() == i:
        print('Acertou o Nro', i)
        break
else:
    print('Não acertou o Nro')
