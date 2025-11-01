import sys
import os

sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lib')
sys.path.append('/Applications/Python_3.13/proga/py_labs/data/lab_04')
from text import *
from io_txt_csv import *

t = read_text("/Applications/Python_3.13/proga/py_labs/data/lab_04/text.txt")
n = normalize(t,True,True)
token = tokenize(n)
c_q = count_freq(token)
top = top_n(c)

print('Всего слов: ',len(token))
print('Уникальных слов: ',len(c_q))
print('Топ - 5: ')
for i in sorted((top), key=lambda item: item[1], reverse = True):
    print(f'{i[0]}: {i[1]}')

write_csv(top,'data/report.csv')