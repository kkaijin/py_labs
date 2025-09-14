minute = input('Минуты: ')
minute = int(minute)
print(f'{minute//60}:{minute-(minute//60)*60:02d}')