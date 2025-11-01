import sys
import os


sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lib')
from text import *

text = input()
token = tokenize(normalize(text,True,False))
c_q = count_freq(tokenize(normalize(text,True,False)))
top = top_n(c_q)
print('Всего слов: ',len(token))
print('Уникальных слов: ',len(c_q))
print('Топ - 5: ')
for i in sorted((top), key=lambda item: item[1], reverse = True):
    print(f'{i[0]}: {i[1]}')