fio = input('ФИО: ')
fio = fio.split()
print('Инициалы:', fio[0][0]+fio[1][0]+fio[2][0])
print('Длина (символов):', len(fio[0])+len(fio[1])+len(fio[2])+2)