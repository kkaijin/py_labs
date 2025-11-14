### ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры)

## Задание 1

```python
from pathlib import Path
import sys
import os
import csv
import argparse

sys.path.append('/Applications/Python_3.13/proga/py_labs/data/lab_04/')
from io_txt_csv import *

sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lib')
from text import *

sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lab_05')
from json_csv import *

def stats(path, n):
    with open(path, 'r') as text:
        content = text.read()
        content_normalize = normalize(content,True,True)
        content_tokenize = tokenize(content_normalize)
        content_freq = count_freq(content_tokenize)
        content_top = top_n(content_freq, n)
        for i in content_top:
            print(*i)
        input()

def cat(path,n):
    with open(path,'r') as text:
        content = text.read()
        content_normalize = normalize(content,True,True)
        content_tokenize = tokenize(content_normalize)
    for i in range(len(content_tokenize)):
        print(i+1, content_tokenize[i])



def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """
        """ Реализация команды stats """
        cat(args.input,args.n)
    elif args.command == "stats":
        
        """ Реализация команды stats """
        stats(args.input,args.top)

input()
main()
```

![Картинка1](../../images/lab_06/task1_1.png)
![Картинка1](../../images/lab_06/task1_2.png)
![Картинка1](../../images/lab_06/task1_2.2.png)

## Задание 2

```python
from pathlib import Path
import sys
import os
import csv
import argparse

sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lab_05')
from json_csv import *

sys.path.append('src/lab_05')
from csv_xlsx import *

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """

    match args.cmd:
        case 'json2csv':
            json_to_csv(args.input, args.output)
        case 'csv2json':
            csv_to_json(args.input, args.output)
        case 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
    print('work')
    input()

main()
```

![Картинка1](../../images/lab_06/task2_1.png)
![Картинка1](../../images/lab_06/task2_1.2.png)
![Картинка1](../../images/lab_06/task2_2.png)
![Картинка1](../../images/lab_06/task2_2.2.png)
![Картинка1](../../images/lab_06/task2_2.png)
![Картинка1](../../images/lab_06/task2_3.png)