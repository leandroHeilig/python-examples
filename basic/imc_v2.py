peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura:'))

imc = peso / altura ** 2

if (imc < 17):
    print('Peso muito abaixo do ideal. Seu IMC é: {}'.format(imc))
elif (imc >= 17 and imc <= 18.49):
    print("Peso está abaixo do ideal. Seu IMC é: {}".format(imc))
elif (imc >= 18.5 and imc <= 24.99):
    print("Peso está na faixa ideal. Seu IMC é: {}".format(imc))
elif (imc >= 25 and imc <= 29.99):
    print("Peso está acima da faixa ideal. Seu IMC é: {}".format(imc))
elif (imc >= 30 and imc <= 34.99):
    print("Peso está acima na faixa Obsedidade I. Seu IMC é: {}".format(imc))
elif (imc >= 35 and imc <= 39.99):
    print("Peso está acima na faixa Obsedidade II. Seu IMC é: {}".format(imc))
else:
    print("Seu peso está na faixa de Obesidade III(Mórbida).',\
          'Seu IMC é: {}".format(imc))
