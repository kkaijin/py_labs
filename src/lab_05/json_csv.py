import json
from pathlib import Path
import sys
import os
import csv

sys.path.append('/Applications/Python_3.13/proga/py_labs/data/lab_04/')
from io_txt_csv import *

sys.path.append('/Applications/Python_3.13/proga/py_labs/src/lib')
from text import *

def json_to_csv(path: str | Path, path_json: str | Path) -> None:
    read_text(path)
    with open(path, 'r') as json_file:

        data_json = json_file.read()
    data = json.loads(data_json)
    if type(data) == list:
        data_n = []
        for i in data:
            data_tup = []
            for k,v in i.items():
                data_tup.append(str(v))
            data_n.append(tuple(data_tup))
        write_csv(data_n, path_json,('name','age','city'))
    else:
        for k,v in data.items():
                data[k] = str(v)
        data_n = top_n(data)
        write_csv(data_n, path_json,('age'))

    
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    if read_text(csv_path) != None:
         return

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        """
            csv.DictWriter
        """
        data_csv = []
        
        csvreader = csv.reader(f)
        for row in csvreader:
            data_csv.append(row)
        data_dict_csv = []
        for i in range(len(data_csv)):
            dict_csv = {}
            if i != 0:
                for j in range(len(data_csv[0])):
                        dict_csv[f'{data_csv[0][j]}'] = data_csv[i][j]
                data_dict_csv.append(dict_csv)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data_dict_csv, f, ensure_ascii=False, indent=4)
        
        

# path_json = Path('/Applications/Python_3.13/proga/py_labs/data/samples/people.json')
path_csv = Path('/Applications/Python_3.13/proga/py_labs/data/samples/cities.csv')
path_json = Path('/Applications/Python_3.13/proga/py_labs/data/samples/people.json12')

if __name__ == '__main__':
    json_to_csv(path_json, '/Applications/Python_3.13/proga/py_labs/data/out/people_fron_json.csv')
    csv_to_json(path_csv,'/Applications/Python_3.13/proga/py_labs/data/out/people_from_csv.json')