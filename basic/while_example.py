from random import randint

informed_number = -1
secret_number = randint(0, 9)

while informed_number != secret_number:
    informed_number = int(input('Informe o número:'))

print('O Número secreto {} foi encontrado. '.format(secret_number))
