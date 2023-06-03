def get_weekday_or_weekend(weekday):
    days = {
        1: 'fim de semana',
        2: 'dia de semana',
        3: 'dia de semana',
        4: 'dia de semana',
        5: 'dia de semana',
        6: 'dia de semana',
        7: 'fim de semana',
    }
    return days.get(weekday, 'Ops! Dia inválido')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia} : {get_weekday_or_weekend(dia)}')
