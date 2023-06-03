'''Dicionário'''
produtos = {'descrição': 'semente de soja',
            'preço': 35.025, 'UM': 'sacas', 'estoque': 854}

for chave in produtos.keys():
    print(chave)

for valores in produtos.values():
    print(valores)

for chave, valor in produtos.items():
    print(chave, '=', valor)
