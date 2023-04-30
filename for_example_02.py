palavra = 'pindamonhangaba'
for letra in palavra:
    print(letra, end=',')

print("\n")

'''Listas'''
guitarristas = ['George Harrison', 'Tony Iommi',
                'Ritchie Blackmore', 'The Edge', 'Jimmy Hendrix']

for nome in guitarristas:
    print(nome)

for indice, nome in enumerate(guitarristas):
    print(f'({indice + 1})', nome)


'''Tupla'''
weekdays = ('Domingo', 'Segunda', 'Terça',
            'Quarta', 'Quinta', 'Sexta', 'Sábado')

for day in weekdays:
    print(f'Hoje é {day}')

'''Set'''
for value in {12, 15, 65, 90, 98, 76, 32}:
    print(value)
