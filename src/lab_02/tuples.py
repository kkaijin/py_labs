def format_record1(t):
    if len(t[0]) == 0 or len(t[1]) == 0 or type(t[2]) != float:
        raise TypeError
    fio = ''
    for i in t:
        s = i.split()
        for j in range(len(s)):
            if j == 0:
                fio = fio+s[j].title()+' '
            else:
                fio = fio+s[j][0].title()+'.'
        break
    return f'{fio}, гр. {t[1]}, GPA {"{:.2f}".format(round(t[2],2))}'

print(format_record1(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record1(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record1(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record1(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record1((" ", "", '098')))
