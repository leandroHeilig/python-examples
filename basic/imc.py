peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura:'))

imc = peso / altura ** 2

if (imc < 20):
    print('Seu peso está abaixo do ideal. Seu IMC é: {}'.format(imc))
else:
    if (imc >= 20 and imc <= 25):
        print("Seu peso está na faixa ideal. Seu IMC é: {}".format(imc))
    else:
        print('Seu peso está acima do ideal. Seu IMC é: {}'.format(imc))
