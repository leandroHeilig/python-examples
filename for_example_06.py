FORBIDEN_WORDS = {'futebol', 'religião', 'política', 'bolsonaro', 'lula'}
text_to_test = ['João gosta de Futebol',
                'A festa foi legal',
                'fã de bolsonaro ou de lula tem problema',
                ]

for text in text_to_test:
    found = False
    for word in text.lower().split():
        print('Existe ao menos uma proibida na frase', word)
        found = True
        break
    if not found:
        print('Esse texto está autorizado. Não vai gerar polêmicas', text)
